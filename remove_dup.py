# website https://gist.github.com/teomaragakis/cb187d880c9a3ca2c8a2
filename = "my_hosts.txt"
with open(filename, "r") as f:
    content = f.read()

urls = [line.strip().split()[1].strip() for line in content.split("\n")]
urls = sorted(list(set(urls)))

with open(filename, "w") as f:
    f.write("\n".join([f"172.0.0.1 {url}" for url in urls]))
