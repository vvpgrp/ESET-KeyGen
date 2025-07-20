## 1. How to generate multiple keys per run
Add a command-line argument: ```--repeat {number}```

```{number}``` - Instead, enter the number of keys

---

## 2. How to use a proxy
Since ```v1.5.5.0``` support for proxy list has been added, for this purpose a command line argument ```--proxy-file {string}``` was created in which ```{string}``` is the path to the file in which your proxies are described.

By default, the program reads a file named **proxies.txt** in the current working directory (from which you started the program). 

---

The syntax of such a file is as follows:

```
scheme:host:port:username:password
scheme:host:port:username:password
scheme:host:port:username:
scheme:host:port::
```

Example (these are not real addresses)
```
http:123.123.123.123:123:user1:pass22
https:101.100.157.125:199:user2:pass33
https:101.100.157.125:199:user2:
https:101.100.157.125:199::
```

---

Proxies with and without authorization are supported, if your proxy requires a password and username,
the syntax will be ```scheme:host:port:username:password```, if not, then ```scheme:host:port::```.

Also if there is an error in any line, it will simply be ignored.

Also if you have entered not real data, the console will say that this proxy is used, but in fact will be used real IP address.

During generation, the console will contain all the information about which proxy is being used (username and password will not be shown in the console or in the logs, so everything is private).

The proxy is changed in two cases:
  * If the program detected that the proxy was banned
  * If the error of generation by this proxy occurred more than 3 times.

If the program used all proxies, it will switch to the original IP. 

#### I strongly recommend using this function together with the ```--repeat``` argument!!!

#### AND MOST IMPORTANTLY, PROXY WORKS ONLY WITH **GOOGLE CHROME** BROWSER!!!
---

## 3. Generation using implemented email APIs
> Also, if you see a message like **[INPT]** in the console, it means that you need to do keyboard input into the console!

---

<details>
  <summary>ESET HOME Security Premium</summary>
  
  1. Run main.py or executable file or use [MBCI](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/wiki/MBCI-Inferface.md):
  ```
  python main.py --chrome --key
  ```
  ```
  ESET-KeyGen_v1.5.5.7_win64.exe --chrome --key
  ```
  > File name is unique for each version! Do not copy the above command. This is an example!

  2. Wait until you will see the license data
  > This information will also be written to a file named "Today date - ESET KEYS.txt"

  ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/key_run_win.png)
</details>

<details>
  <summary>ESET Small Business Security</summary>
  
  1. Run main.py or executable file or use [MBCI](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/wiki/MBCI-Inferface.md):
  ```
  python main.py --chrome --small-business-key
  ```
  ```
  ESET-KeyGen_v1.5.5.7_win64.exe --chrome --small-business-key
  ```
  > File name is unique for each version! Do not copy the above command. This is an example!

  2. Wait until you will see the license data
  > This information will also be written to a file named "Today date - ESET KEYS.txt"

  ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/small_business_key_run_win.png)
</details>

<details>
  <summary>ESET PROTECT Advanced (ESET Endpoint Security + ESET Server Security, ESET LiveGuard Advanced for Endpoint Security + Server Security, ESET Mobile Threat Defense, ESET Full Disk Encryption)</summary>
  
  1. Run main.py or executable file use [MBCI](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/wiki/MBCI-Inferface.md):
  ```
  python main.py --chrome --advanced-key
  ```
  ```
  ESET-KeyGen_v1.5.5.7_win64.exe --chrome --advanced-key
  ```
  > File name is unique for each version! Do not copy the above command. This is an example!

  > **Works ONLY if you use the ```--custom-email-api``` argument or the following ```Email APIs```: ```mailticking```, ```fakemail```, ```inboxes```, ```incognitomail```**

  2. Wait until appears you will see *"Solve the captcha on the page manually!!!"*. Next, you will see a captcha with text input in the browser window created. You solve it and then just do nothing, the algorithm will do everything for you!

  3. Wait until you will see the license data
  > This information will also be written to a file named "Today date - ESET KEYS.txt"

  ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/endpoint_key_run_win.png)
</details>

<details>
  <summary>ESET VPN (It's not working right now!!!)</summary>
  
  1. Run main.py or executable file or use [MBCI](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/wiki/MBCI-Inferface.md):
  ```
  python main.py --chrome --vpn-codes
  ```
  ```
  ESET-KeyGen_v1.5.5.7_win64.exe --chrome --vpn-codes
  ```
  > File name is unique for each version! Do not copy the above command. This is an example!

  2. Wait until you will see the license data and vpn codes
  > This information will also be written to a file named "Today date - ESET KEYS.txt"

  ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/vpn_codes_run_win.png)
</details>

---

## 4. Generation using your email provider

<details>
  <summary>ESET HOME Security Premium | ESET Small Business Security</summary>
  
  #### ESET HOME Security Premium
  1. Run main.py or executable file use [MBCI](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/wiki/MBCI-Inferface.md):
  ```
  python main.py --chrome --key --custom-email-api
  ```
  ```
  ESET-KeyGen_v1.5.5.7_win64.exe --chrome --key --custom-email-api
  ```
  > File name is unique for each version! Do not copy the above command. This is an example!

  #### ESET Small Business Security
  1. Run main.py or executable file use [MBCI](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/wiki/MBCI-Inferface.md):
  ```
  python main.py --chrome --small-business-key --custom-email-api
  ```
  ```
  ESET-KeyGen_v1.5.5.7_win64.exe --chrome --small-business-key --custom-email-api
  ```
  > File name is unique for each version! Do not copy the above command. This is an example!

  2. Then in the console you'll see *"Enter an email address you have access to"* and you'll need to enter a real existing email address that you can read incoming emails to. I suggest using a temporary email for this, such as [TempMail](https://temp-mail.org)
  > Then the algorithm will continue as in the first method

  3. After some time in the console you will see the message *"Enter the link to activate your account, it will come to the email address you provide"*, here you need to go to your email and find mail in inbox (you will have to wait)
    
     **FROM: info@product.eset.com**
     
     **SUBJECT: Account Confirmation**

     Then open that email and copy the link that is in the button (right click on the button, copy link address) and paste it into the console. If you have done everything correctly, the generation will complete successfully!

     ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/activated_href_esethome.png)

  4. Wait until appears you will see the license data 
  > This information will also be written to a file named "Today date - ESET KEYS.txt"

  #### ESET HOME Security Premium
  ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/key_run_win_custom_email_api.png)

  #### ESET Small Business Security
  ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/small_business_key_run_win_custom_email_api.png)
</details>

<details>
  <summary>ESET PROTECT Advanced (ESET Endpoint Security + ESET Server Security, ESET LiveGuard Advanced for Endpoint Security + Server Security, ESET Mobile Threat Defense, ESET Full Disk Encryption)</summary>
  
  1. Run main.py or executable file use [MBCI](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/wiki/MBCI-Inferface.md):
  ```
  python main.py --chrome --advanced-key --custom-email-api
  ```
  ```
  ESET-KeyGen_v1.5.5.7_win64.exe --chrome --advanced-key --custom-email-api
  ```
  > File name is unique for each version! Do not copy the above command. This is an example!

  2. Then in the console you'll see *"Enter an email address you have access to"* and you'll need to enter a real existing email address that you can read incoming emails to. I suggest using a temporary email for this, such as [TempMail](https://temp-mail.org)
  > Then the algorithm will continue as in the first method

  3. Wait until appears you will see *"Solve the captcha on the page manually!!!"*. Next, you will see a captcha with text input in the browser window created. You solve it and then just do nothing, the algorithm will do everything for you!

  4. After some time in the console you will see the message *"Enter the link to activate your account, it will come to the email address you provide"*, here you need to go to your email and find mail in inbox (you will have to wait)

     **FROM: noreply@protecthub.eset.com**

     **SUBJECT: Welcome to ESET PROTECT Hub**

     Then open that email and copy the link that is in the button (right click on the button, copy link address) and paste it into the console. If you have done everything correctly, the generation will complete successfully!

     ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/activated_href_protecthub.png)

  5. Wait for the inscription *"Wait for a message to your e-mail about successful key generation!!!"*

  ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/endpoint_key_run_win_custom_email_api.png)

  6. Wait for the license data to appear (you will have to wait)
  This information will be sent to your e-mail in the form of a letter in the format of:
     
     **FROM: noreply@orders.eset.com**

     **SUBJECT: Thank you for purchasing ESET PROTECT Advanced**

  Then open that email, scroll down a bit and you'll see the license key!

  ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/protecthub_license_data_message.png)
</details>

<details>
  <summary>ESET VPN (It's not working right now!!!)</summary>
  
  1. Run main.py or executable file use [MBCI](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/wiki/MBCI-Inferface.md):
  ```
  python main.py --chrome --vpn-codes --custom-email-api
  ```
  ```
  ESET-KeyGen_v1.5.5.7_win64.exe --chrome --vpn-codes --custom-email-api
  ```
  > File name is unique for each version! Do not copy the above command. This is an example!

  2. Then in the console you'll see *"Enter an email address you have access to"* and you'll need to enter a real existing email address that you can read incoming emails to. I suggest using a temporary email for this, such as [TempMail](https://temp-mail.org)
  > Then the algorithm will continue as in the first method

  3. After some time in the console you will see the message *"Enter the link to activate your account, it will come to the email address you provide"*, here you need to go to your email and find mail in inbox (you will have to wait)
    
     **FROM: info@product.eset.com**
     
     **SUBJECT: Account Confirmation**

     Then open that email and copy the link that is in the button (right click on the button, copy link address) and paste it into the console. If you have done everything correctly, the generation will complete successfully!

     ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/activated_href_esethome.png)

  4. Wait for the inscription *"Wait for a message to your e-mail about instructions on how to set up the VPN!!!"*
  
  ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/vpn_codes_run_win_custom_email_api.png)
    
  5. Wait for the **VPM Codes** to appear (you will have to wait)
  This information will be sent to your e-mail in the form of a letter in the format of:
     
     **FROM: info@product.eset.com**

     **SUBJECT: ESET VPN - Setup instructions**
  
  Then open that email, scroll down a bit and you'll see the **VPN Codes**!
  
  ![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/vpn_codes_message.png)
</details>

---

## 5. Unbinding license key from ESET ProtectHub account
Once the **ProtectHub** key has been successfully generated and obtained from the site, you can delete it from the created account (this will not affect the functionality of the key).
This will allow you to bind the key to another **ProtectHub** account (sometimes this can be useful).

To do this, enter ```Y``` to confirm and ```N``` to decline after the message appears in the console:

![Windows](https://github.com/rzc0d3r/ESET-KeyGen/blob/main/img/unbinding_protecthub_key.png)
