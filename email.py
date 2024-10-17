import subprocess


def check_email(email):
    try:
        # Run the holehe command
        result = subprocess.run(
            ["holehe", email],
            capture_output=True,
            text=True,
            check=True,  # This will raise an exception if the command fails
        )
        return result.stdout

    except subprocess.CalledProcessError as e:
        return f"Error occurred: {e}"

    except FileNotFoundError:
        return "holehe command not found. Please make sure it is installed."


email = input("Enter email: ")
response = check_email(email)
print(response)
