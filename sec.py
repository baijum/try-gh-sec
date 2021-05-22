import os
import base64

def main():
    repo = os.environ.get("REPO")
    print(f"Hello! {repo}", repo)
    repob64 = base64.b64encode(bytes(repo, "utf-8"))
    print(f"Hello! {repob64}", repob64)
    repob64d = base64.b64decode(repob64)
    print(f"Hello! {repob64d}", repob64d)

if __name__ == "__main__":
    main()
