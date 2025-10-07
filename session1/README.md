# Agentic AI in DevOps: Session One

Welcome to the Agentic AI Bootcamp! This is a hands-on program designed for complete beginners to learn how to integrate AI into real-world DevOps workflows.

## Prerequisites

To get started, you'll need the following:

1. **Python 3**: Ensure you have Python 3 installed on your system. You can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. **Git**: Install Git, a version control system, on your machine. You can download it from the official Git website: [https://git-scm.com/downloads](https://git-scm.com/downloads)
3. **OpenAI API Key**: Obtain an API key from the OpenAI platform to use their AI models. You can sign up and create a key at [https://openai.com/](https://openai.com/)
4. **(Optional) Ollama**: If you'd like to use the Ollama AI model instead of OpenAI, you'll need to install it. You can find instructions at [https://github.com/anthropic-research/ollama](https://github.com/anthropic-research/ollama)
5. **Terraform**: Download and install Terraform, an Infrastructure as Code (IaC) tool, from the official HashiCorp website: https://www.terraform.io/downloads.html
6. **AWS CLI**: Set up the AWS Command Line Interface (CLI) on your machine. You can find the instructions on the AWS documentation: https://aws.amazon.com/cli/


## Session 1 — Setup + Log Troubleshooting

In this session, you'll learn how to:

1. **Run your first AI agent (agent_unified.py)** to generate Kubernetes YAML
2. **Build a log-troubleshooting agent (agent_log_troubleshooter.py)** to analyze system logs

### Script 1: agent_unified.py

This script asks AI to generate a Kubernetes Deployment YAML.

**Explanation**:
1. Import libraries (os, subprocess, OpenAI).
2. Check if the backend is OpenAI or Ollama.
3. Define the `ask_llm` function to talk to the AI.
4. If using OpenAI, send the prompt and return the reply.
5. If using Ollama, run the local model.

### Script 2: agent_log_troubleshooter.py

This script collects Linux system information and asks the AI to diagnose problems.

**Explanation**:
1. Import libraries.
2. Define the helper `sh()` function to run shell commands.
3. Define the `gather()` function to collect system data (disk, memory, uptime, logs, errors).
4. Send the combined data to the AI using `ask_llm`.
5. Print the AI's troubleshooting summary and commands.

## Getting Started

1.**Terraform Setup**:
* Create a new directory for your DevOps project.
* Inside the directory, create a new file named main.tf.
* Add the following Terraform code to provision an EC2 instance:
```bash
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "devops_instance" {
  ami           = "ami-0aa7d40eeae50c9a9" # Amazon Linux 2 AMI
  instance_type = "t2.micro"
  key_name      = "your-ec2-key-pair"

  tags = {
    Name = "DevOps-Instance"
  }
}
```
* Replace "your-ec2-key-pair" with the name of your existing EC2 key pair or create a new one.
* Run terraform init to initialize the Terraform working directory.
* Run terraform apply to provision the EC2 instance.

2. **Clone the Repository**:
```bash
git clone https://github.com/Here2ServeU/agentic_ai_3_sessions.git
cd agentic_ai_3_sessions
```

3. **Set the OpenAI API Key**:
```bash
export OPENAI_API_KEY=your_openai_api_key
```

4. **Run the Scripts**:

a. Using OpenAI:
   ```
   cd session1
   python3 agent_unified.py
   python3 agent_log_troubleshooter.py
   ```

b. Using Ollama:
   ```
   cd session1
   export AGENT_BACKEND=ollama
   python3 agent_unified.py
   python3 agent_log_troubleshooter.py
   ```

**Remember, you can switch between OpenAI and Ollama by setting the `AGENT_BACKEND` environment variable. Enjoy your journey into the world of Agentic AI in DevOps!**

5. **Clean Up**
* Use the following command to destroy your EC2 instance:
```bash
terraform destroy -auto-approve
```

---

## About Me  

DevOps, Cloud, and SRE Engineer with AI integration expertise.  
Currently pursuing a PhD in Computer Science (AI & ML in Healthcare, Cloud, and DevOps).  

---

## Skills & Certifications  

![AWS](https://img.shields.io/badge/AWS-orange?logo=amazon-aws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-blue?logo=microsoft-azure&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326ce5?logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?logo=terraform&logoColor=white)
![OpenAI](https://img.shields.io/badge/AI-OpenAI-412991?logo=openai&logoColor=white)

![AWS Solutions Architect](https://img.shields.io/badge/Cert-AWS%20SA-orange?logo=amazon-aws&logoColor=white)
![Azure Solutions Architect Expert](https://img.shields.io/badge/Cert-Azure%20SA%20Expert-blue?logo=microsoft-azure&logoColor=white)
![Terraform Associate](https://img.shields.io/badge/Cert-Terraform%20Assoc-844FBA?logo=terraform&logoColor=white)
![CKA](https://img.shields.io/badge/Cert-CKA-326ce5?logo=kubernetes&logoColor=white)
![PhD-CS](https://img.shields.io/badge/PhD-CS%20(In%20Progress)-lightgrey)

---

[LinkedIn](https://linkedin.com/in/ready2assist) | [GitHub](https://github.com/Here2ServeU)

---
