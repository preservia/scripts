import hashlib

def generate_preserve_id(metadata_string: str) -> str:
    """
    Generate a 7-digit PreserveID from a MetadataString.
    Format: TYPEPREFIX + 7 digits (e.g., P7395601)
    """
    try:
        shortname, content_type, platform, version = metadata_string.split(":")
    except ValueError:
        raise ValueError("MetadataString must be formatted as SHORTNAME:TYPE:PLATFORM:VERSION")

    hash_value = hashlib.sha256(metadata_string.encode()).hexdigest()
    numeric_hash = int(hash_value, 16) % 10_000_000
    preserve_code = f"{numeric_hash:07d}"
    preserve_id = f"{content_type[0].upper()}{preserve_code}"
    return preserve_id


if __name__ == "__main__":
    metadata = input("Enter MetadataString: ")
    print("PreserveID:", generate_preserve_id(metadata))