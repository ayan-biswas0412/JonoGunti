# Jono-Gunti (The People Counter)
This is a people counter program that detects the number of people in a single place by analysing video via IP Camera of Drone or Mobile device or it can also analyze a recorded video file.


* After Cloning the Repository Just Copy and paste this code to the terminal 
(Open the terminal from inside this downloaded folder)

```python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/example_01.mp4 --output output.avi```

* If all are set then you can connect it with the IP Camera if your chosen device (Drones , CCTVs or Mobile Devices ).

**To Connect with another devices just follow this steps .**
(Here connection with a mobile device is shown ).

1. Download [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam) app from Google   
   Play store. 

2. Then Open the app.

3. Select **Start Server**

4. Note Down the IPv4 address.

5. Copy and Paste the following code in terminal (Open the terminal from inside this downloaded folder).
   
   ```python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --output output.avi```

6. Enter the IPv4 address of the camera in the terminal when prompted and start Surveillancing


  
































<a href="https://github.com/ayan-biswas0412/JonoGunti/pulls">![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/ayan-biswas0412/JonoGunti?logo=git&logoColor=white)</a> 
<a href="#">![GitHub contributors](https://img.shields.io/github/contributors/ayan-biswas0412/JonoGunti?logo=github)</a>
[![GitHub issues](https://img.shields.io/github/issues/ayan-biswas0412/JonoGunti?logo=github)](https://github.com/ayan-biswas0412/JonoGunti/issues) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat&logo=git&logoColor=white)](https://github.com/ayan-biswas0412) 
[![GitHub last commit](https://img.shields.io/github/last-commit/ayan-biswas0412/JonoGunti?logo=github)](https://github.com/jadavpur-university-ed-cell)
