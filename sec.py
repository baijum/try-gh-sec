import os

def main():
    repo = os.environ.get("REPO")
    print(f"Hello! {repo}", repo)

if __name__ == "__main__":
    main()
