import json
from jwcrypto import jwk

try:
    with open("openemr_public.pem", "rb") as f:
        pem_data = f.read()
    pub = jwk.JWK.from_pem(pem_data)
except FileNotFoundError:
    print("Error: The file 'openemr_public.pem' was not found.")
    exit()

jwk_dict = pub.export_public(as_dict=True)
jwk_json_string = json.dumps(jwk_dict, indent=4)

output_filename = "openemr_public_jwk.txt"
try:
    with open(output_filename, "w") as outfile:
        outfile.write(jwk_json_string)
    
    print(f"Successfully exported public key to {output_filename}")

except Exception as e:
    print(f"An error occurred while writing to the file: {e}")