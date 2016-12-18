## Note 

If you want to run this on a clean Ubuntu 16.04 AWS AMI then you may have to installl `python-minimal` on the remote host since there is no python by default on the server. After that you can run the Ansible playbook from your laptop.

```
sudo apt update
sudo apt install python-minimal
```

## Requirements

- Check if Apache2 was installed
- Install only when there is no Apache2 on the server
- Make sure that the service was started by the end

## How to run

Need Ansible 2.x http://docs.ansible.com/ansible/intro_installation.html

```
# Using pip
sudo pip install ansible
```

Verify

```
ansible --version
ansible 2.2.0.0
```

Update the `hosts` file with the IP and the setting of SSH

```
[all]
54.211.160.124 ansible_user=ubuntu ansible_ssh_private_key_file=/home/xyz/.ssh/id_rsa ansible_port=22
```

Run the ansible-playbook

```
ansible-playbook -i hosts main.yml -v
```


