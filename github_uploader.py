"""
Upload Project directly to GitHub using GitHub REST API.
Does NOT require git to be installed on your computer.
"""

import os
import sys
import base64
import json
import urllib.request
import urllib.error


def upload_to_github():
    print("=" * 60)
    print("      ELECTRICITY USAGE PREDICTOR - GITHUB UPLOADER")
    print("=" * 60)
    print("Aap direct GitHub par project upload kar sakte hain!\n")
    print("Requirement: GitHub Personal Access Token (PAT)")
    print("Token lene ka tarika: https://github.com/settings/tokens/new (Check 'repo' scope)\n")

    token = input("Enter your GitHub Personal Access Token: ").strip()
    if not token:
        print("Token enter nahi kiya gaya. Aborted.")
        return

    repo_name = input("Enter Repository Name (Default: Electricity-Usage-Predictor-PS64): ").strip()
    if not repo_name:
        repo_name = "Electricity-Usage-Predictor-PS64"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Antigravity-Python-Client"
    }

    # Step 1: Create repository
    print(f"\n[1/3] Creating repository '{repo_name}' on GitHub...")
    create_repo_url = "https://api.github.com/user/repos"
    repo_data = {
        "name": repo_name,
        "description": "Electricity Usage Predictor (PS No. 64) - Rungta International Skills University",
        "private": False
    }

    req = urllib.request.Request(
        create_repo_url,
        data=json.dumps(repo_data).encode("utf-8"),
        headers=headers,
        method="POST"
    )

    repo_full_name = None
    try:
        with urllib.request.urlopen(req) as resp:
            resp_data = json.loads(resp.read().decode("utf-8"))
            repo_full_name = resp_data["full_name"]
            print(f">>> Repository created: https://github.com/{repo_full_name}")
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        if "name already exists" in err_msg:
            # Get authenticated username
            user_req = urllib.request.Request("https://api.github.com/user", headers=headers)
            with urllib.request.urlopen(user_req) as uresp:
                user_info = json.loads(uresp.read().decode("utf-8"))
                repo_full_name = f"{user_info['login']}/{repo_name}"
            print(f">>> Repository '{repo_full_name}' already exists. Using existing repo.")
        else:
            print(f"Error creating repository: {e} - {err_msg}")
            return

    # Step 2: Upload all files
    files_to_upload = [
        "electricity_predictor.py",
        "test_runner.py",
        "usage.csv",
        "testcase1_normal.csv",
        "testcase2_boundary.csv",
        "testcase3_invalid.csv",
        "testcase4_scenario.csv",
        "usage_trend_plot.png",
        "PROJECT_REPORT.html",
        "PROJECT_REPORT.md",
        "README.md",
        "requirements.txt",
        ".gitignore"
    ]

    print(f"\n[2/3] Uploading {len(files_to_upload)} project files to GitHub...")

    for fname in files_to_upload:
        if not os.path.exists(fname):
            continue

        with open(fname, "rb") as f:
            content_bytes = f.read()
        content_b64 = base64.b64encode(content_bytes).decode("utf-8")

        file_api_url = f"https://api.github.com/repos/{repo_full_name}/contents/{fname}"

        # Check if file already exists to get SHA for update
        sha = None
        check_req = urllib.request.Request(file_api_url, headers=headers)
        try:
            with urllib.request.urlopen(check_req) as c_resp:
                c_data = json.loads(c_resp.read().decode("utf-8"))
                sha = c_data.get("sha")
        except urllib.error.HTTPError:
            pass

        put_payload = {
            "message": f"Upload {fname}",
            "content": content_b64
        }
        if sha:
            put_payload["sha"] = sha

        put_req = urllib.request.Request(
            file_api_url,
            data=json.dumps(put_payload).encode("utf-8"),
            headers=headers,
            method="PUT"
        )

        try:
            with urllib.request.urlopen(put_req) as p_resp:
                print(f"  + Uploaded: {fname} [OK]")
        except Exception as e:
            print(f"  - Failed {fname}: {e}")

    print("\n" + "=" * 60)
    print(f"[3/3] PROJECT SUCCESSFULLY UPLOADED TO GITHUB!")
    print(f"Repository Link: https://github.com/{repo_full_name}")
    print("=" * 60)


if __name__ == "__main__":
    upload_to_github()
