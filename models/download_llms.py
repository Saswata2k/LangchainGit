from huggingface_hub import hf_hub_download
import joblib

REPO_ID = "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
FILENAME = "mistral-7b-instruct-v0.2.Q4_K_M.gguf"

if __name__ == "__main__":
    model = joblib.load(
        hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
    )