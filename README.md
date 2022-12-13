<!-- This should be the location of the title of the repository, normally the short name -->
# az-dns-update - Python script to update a dns A record on Azure DNS

<!-- Build Status, is a great thing to have at the top of your repository, it shows that you take your CI/CD as first class citizens -->
<!-- [![Build Status](https://travis-ci.org/jjasghar/ibm-cloud-cli.svg?branch=master)](https://travis-ci.org/jjasghar/ibm-cloud-cli) -->

<!-- Not always needed, but a scope helps the user understand in a short sentance like below, why this repo exists -->
## Scope

The purpose of this repository is to provide example code to demonstrate how an A DNS record can be updated from a running virtual machine. This is useful when the server has a varying public IP address as received from an ISP which needs to be resolved by other clients through a consistent DNS name. Common use cases are CCTV DVRs, SOHO/Branch all-in-one servers.


<!-- A more detailed Usage or detailed explaination of the repository here -->
## Usage

This script queries the public IP that is visible for the machine, even if it is behind a NAT by connecting to a service "myip" on the api endpoint https://sayan-tech-api-py.azurewebsites.net/api/

The code for the API endpoint is included in the folder `myip` and can be deployed on Azure using Azure Functions.

The ip is thereafter updated to the A record for the DNS entry indicated in the dns_client api call.

Key files:

azure_dns.py: Script for getting the retrieving public IP address and updating DNS record

Execution:

Please make azure_dns.py an executable by using chmod +x

Execute by running it as ./azure_dns.py
ml --vault-id @prompt

Configurations:

subscription_id: Subscription ID on Azure where the DNS service is attached
tenant_id: Valid tenant ID of the IAM/AD user
client_id: Valid client ID of the IAM/AD user
client_secret: Valid client secret of the IAM/AD user

The IAM/AD user should have the rights to update the DNS entry.

This script can be executed on a regular basis by making a cron tab entry on a linux system

Cleaning up:

Remove the cron tab entry, if applicable, to prevent the script from running on a schedule.

<!-- License and Authors is optional here, but gives you the ability to highlight who is involed in the project -->
## License & Authors

If you would like to see the detailed LICENSE click [here](LICENSE).

- Author: Sayan A Ghosh <sayan.acharya.ghosh@kyndryl.com>
- Maintainer: Sayan A Ghosh <sayan.acharya.ghosh@kyndryl.com>

```text
Copyright:: 2022-2022 Kyndryl, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
