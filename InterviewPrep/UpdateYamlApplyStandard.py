import copy
import yaml

# The goal is to open the yaml file, read the contents
# Update the version to v2
# Enforce min replica standard

def update_config(input_file, output_file, new_tag, min_replicas=2):
    with open(input_file, "r") as f:
        data = yaml.safe_load(f)

    dataCopy = copy.deepcopy(data)

    services = dataCopy["services"]

    for service, config in services.items():
        
        # Get and update the image tag
        image = config["image"]
        baseVersion = ""
        if image:
            if ":" in image:
                baseVersion = image.split(":")[0]
        config["image"] = baseVersion + ":" + new_tag

        # Get and update the replica count
        replicaCount = config["replicas"]
        config["replicas"] = max(replicaCount, min_replicas)

    with open(output_file, "w") as f:
        yaml.safe_dump(dataCopy, f)

def update_config3(input_file, output_file, new_tag, min_replicas=2):
    # Load the file contents into a copy data
    with open(input_file, "r") as f:
        data = yaml.safe_load(f)

    # Safe copy of data
    dataCopy = copy.deepcopy(data)
    
    # Get the services
    services = dataCopy.get("services")

    # Loop for each service
    for service, config in services.items():
        
        # Extract and update values
        image = config.get("image")
        if image:
            if ":" in image:
                imageBaseVersion = image.split(":")[0]
            config["image"] = f"{imageBaseVersion}:{new_tag}"

        replicas = config.get("replicas")
        if replicas:
            if replicas < min_replicas:
                config["replicas"] = min_replicas
    
    # Write back to the file
    with open(output_file, "w") as f:
        yaml.safe_dump(dataCopy, f)

def update_config2(input_file, output_file, new_tag, min_replicas=2):
    with open(input_file, "r+") as f:
        data = yaml.safe_load(f)

    # Defensive copy (optional but good practice)
    dataClone = copy.deepcopy(data)

    services = dataClone.get("services", {})

    for service_name, config in services.items():
        print(f"Service: {service_name}")
        print(f"Config: {config}")

        # Update image tag
        image = config.get("image")
        if image:
            base = image.split(":")[0]
            config["image"] = f"{base}:{new_tag}"

        # Ensure minimum replicas
        replicas = config.get("replicas", 1)
        if replicas < min_replicas:
            config["replicas"] = min_replicas

    # Write back safely
    with open(output_file, "w") as f:
        yaml.safe_dump(dataClone, f, sort_keys=False)


if __name__ == "__main__":
    update_config("UpdateYamlApplyStandard.yaml", "output.yaml", new_tag="v2")