<img src="https://i.ibb.co/vJsFJDr/oie-png-1.png" width="206" height="206">

# Spothole - Artificial Intelligence Powered Pothole Detection, Reporting and Management Solution

## Spothole Core Backend (Object Detection + Flask API)

### Introduction

A major problem being faced by municipalities around the world is maintaining the
condition of roads be it summer, the monsoons (when it is at its worst) or any weather
condition as a matter of fact. And although it’s the responsibility of the authorities to make
sure the roads are free of damage, at times they overlook the problem, and most times don’t
even know that the problem exists. According to “Safety Resource Center”, approximately
3 Billion US Dollars are spent by motorists for repair of blown tires, busted axles, and other
damage to their vehicles. Over the past five years around 16 million drivers across the U.S. have suffered damage
from potholes as per an article from “American Automobile Association (AAA)”


Maintaining the road condition is a challenge with constant weather changes, wear
and tear, low budgets for the municipalities. Also, not to forget keeping people informed is
a task. So, this is an app aimed at solving the challenges mentioned. A reporting system,
where the citizen can capture the scene of an area, which will be fed to a machine learning
model that will geocode, validate and track down potholes in the scene. This has been
achieved by training for object tracking on multiple images and developed using
convolutional neural networks. Users can see the damage on the roads using a
mobile application or through their browsers. A dynamic report is also  generated for the closest authority of concern which they can view and update to
create and manage work orders using their own jurisdiction-based web/mobile app-based
dashboard.

### Motivation
In articles covered by Guardian News & Media potholes took a deadly toll in 2017, claiming almost 10 lives daily. IndiaTimes stated that "Bereaved Father Mr. Dadarao" filled 600 Potholes in Mumbai in memory of son he lost in a road accident! Inshorts reported, potholes killed more people than terrorists reporting 14,926 deaths in road accidents.

When we look at the other side of the world, there is a similar situation as reported by American Automobile Association.

Keeping the roads in good condition along with tracking damages is a challenge with constant changes in weather, low budgets for the municipalities. Not to forget keeping the people informed is a task. This project was aimed at solving the challenges mentioned.

### Important URLs

#### Demo 
Link to Citizen App Demo: https://nirbhay.me/spothole/
Link to Authority App Demo: https://nirbhay.me/spothole.authority/

#### Landing Page 
Link to Landing Page: https://nirbhay.me/spothole/home

#### Citizen App Repository 
Link to Citizen App's Repository: https://github.com/nirbhayph/spothole

#### Authority App Repository 
Link to Authority App's Repository: https://github.com/nirbhayph/spothole.authority

#### Core Backend App Project Structure
Link to Project's Directory Structure: https://nirbhay.me/spothole.core/project_structure/

### Process Description
#### The backend comprises of two main sections. The first being the object detection model built using Darkflow. The second being the Flask API for data exchange between the model built, the database and the frontend. 
##### 1. Object Detection Model
  * As the focus of the application was to create a rest api to automate the process of pothole validation with media files, from the beginning itself a cloud server was used for implementation. A [EC2 Amazon Web Services Instance](https://aws.amazon.com/ec2/instance-types/) was used for this purpose. 
  * AWS EC2 C5 instance (model: c5.xlarge) after choosing Ubuntu 18 which features the Intel Xeon Platinum 8000 series and offers a set of 4vCPUs each with 8 GiB of memory was chosen for training the object detection model. 
  * The model is trained on top of [Darkflow](https://github.com/thtrieu/darkflow)  and built on top of pretrained weights which were obtained from [Darknet](https://pjreddie.com/darknet/). 
  * For crawling images relevant to our label ‘pothole’, images were crawled using the open source google image search package, along with using the serpapi image search tool.
  * In addition to this freely available pothole video feeds to create the dataset were also used. For a near to decent detection result, we should look to collect at least 500+ images. The dataset has been provided with the repository. 
  * In case of video files, we can upload it to our server using an sftp client like Filezilla or by directly using ssh on the terminal of our local machine. The next step was to write a script to slice this uploaded video to images. Python’s  OpenCV (cv2 package and Video Capture Module)  to divide the feed into frames. 
  * Using ‘pip install’ the following dependencies need to be added. [pillow, lxml, jupyter, matplotlib, protobuffer] 
  * To prepare the input files for DarkFlow we need to consider two things. Firstly, we need an RGB image which is encoded as jpeg or png and secondly, we need a list of bounding boxes (xmin, ymin, xmax, ymax) for the image and the class of the object in the bounding box. 
  * Our class, in this case, is ‘pothole’. We then need to label our images with a tool like LabelImg to identify areas of interest with bounding boxes. 
  * LabelImg is a graphical image annotation tool that is written in Python and uses Qt for the graphical interface. 
  * It supports Python 2 and 3. The annotations are saved as XML files in the Pascal VOC format We can split the data to train and test sets before running the training command. 
  * Now the datasets needed for feeding darkflow package in the required format are available.
  * We need to first configure Darkflow by modifying the configuration file and labels.txt file. 
  Then we need to make a copy from cfg/tiny-yolo-voc.cfg and create a cfg/tiny-yolo-voc-1c.cfg file with the same content. Change the line 114 to filters=30 [num * (classes + 5)] and set classes=1 as we have only one class ‘pothole’. 
  * In the label.txt file remove all the labels and just keep the pothole label. 
  * Once done, refer to the training command on this link. [Train Yolo with Darkflow](https://sites.google.com/view/tensorflow-example-java-api/complete-guide-to-train-yolo/train-yolo-with-darkflow), and start training with the dataset created earlier.
  * Using the test sets the model can be verified to check the accuracy of our newly trained object tracking model. This can now also be applied to various snippets of video to highlight the potential of object detection on potholes. Refer to the link mentioned in the above step for the testing command. It also contains options to restart training from a previous checkpoint.
  * We will then proceed to saving the built graph as a protobuf file. Read this link on [Darkflow](https://github.com/thtrieu/darkflow#save-the-built-graph-to-a-protobuf-file-pb) to understand this better. 
  ```
  flow --pbLoad built_graph/yolo.pb --metaLoad built_graph/yolo.meta --imgdir sample_img/
  ```
  * The dataset, the annotation files, the built model have all been provided with the repository for reference. 
  

  





### Feature Stack 
| Feature Name | Screen Name |
| --- | --- |
| Pie Chart (Status Wise Counts) | Dashboard (Analytics Section) |
| Stacked Bar Chart (Status and Severity Wise Reports) | Dashboard (Analytics Section) |
| Deep Learning Powered Media Validated Reports | Dashboard |
| Filterable Datatable for Displaying Zone Wise Reports | Dashboard |
| Export CSV, Filter By Column | Dashboard, Manage Users |
| Search Reports (Datatable) | Dashboard |
| Severity Indicator (0-10) (Update Report) | Update Report |
| Custom Text Area Description Box (For Additional Comments) | View, Update Report |
| Custom Alerts (Single and Multi Actionables) | Update Report - Submit |
| Successful Status Update Email Notification | Update Report |
| Update Report Status Selectable | Update Report |
| Static Image based Geographic Map | View Report |
| Comments Section (Communication Exchange Between Citizen and Authority) | View Report |
| Custom Error Alerts | Update Report |
| Map Legend Indicating Severity Levels | Map View |
| Street View Renderer | Map View |
| Custom Markers for Potholes Distributed by Severity in Authority's Zone | Map View |
| Custom Info Window (When Clicked on Marker) | Map View | 
| Update Report by Clicking Button on Info Window | Map View |
| Map Full Screen View | Map View |
| Heat Map Layer Toggle | Map View |
| Filterable Datatable for Displaying Zone Wise Users | Manage Users |
| Search Users (Datatable) | Manage Users |
| Block Users (Datatable) | Manage Users |
| Email Notifcation on Block / Unblock | Manage Users |
| Profile Details (Avatar, Name , Email Id) | Profile |
| Authority's Summarized Report Statistics Based on Status (Submitted, Approved, Completed, Working, Cancelled) | Profile |
| Custom Random Background | Log In | 
| O-Auth 2.0 Sign In | Log In |
| Only Registered Authority Email Addresses can Sign In | Log In |
| 404, 401 | Error Pages |
| Fixed App Bar | All Screens |
| Left Menu Drawer (App Bar) | All Screens |
| App Bar Menu Icons (App Bar - Float Right) | All Screens |

### Libraries Used
* The Application has been built using React.js
* Material Design has been used throughout the App.
* Material UI Icons have been used for Icons. 
* MUI-Treasury Componenets have been used for additional needs (Like Card View in the Profile Screen)
* Axios has been used for making REST Calls to the Backend.
* GitHub Pages has been used for Static Deployment of the Application. 
* React Google Maps has been used for all Mapping, Heat Mapping, Marker Needs. 
* Google Oauth 2.0 has been used Application Wide for Authentication Purposes. 
* Material UI Datatables are used for Displaying Zone Wise Report Data and Managing Users. 
* Recharts is used for Analytics Needs. 

#### Libarary Details
| Library Name | Version |
| --- | --- |
| @material-ui/core | ^4.9.5 |
| @material-ui/icons | ^4.9.1 |
| @material-ui/lab | ^4.0.0-alpha.45 |
| @mui-treasury/components | ^1.0.0 |
| @mui-treasury/styles | ^1.0.0 |
| @mui-treasury/styling | ^0.2.8 |
| @testing-library/jest-dom | ^4.2.4 |
| @testing-library/react | ^9.5.0 |
| @testing-library/user-event | ^7.2.1 |
| autosuggest-highlight | ^3.1.1 |
| axios | ^0.19.2 |
| bootstrap | ^4.4.1 |
| dateformat | ^3.0.3 |
| gh-pages | ^2.2.0 |
| lodash | ^4.17.15 |
| mui-datatables | ^2.14.0 |
| react | ^16.13.1 |
| react-dom | ^16.13.1 |
| react-filepond | ^7.0.1 |
| react-google-maps | ^9.4.5 |
| react-router | ^5.1.2 |
| react-router-dom | ^5.1.2 |
| react-scripts | 3.4.1 |
| recharts | ^1.8.5 |
| recompose | ^0.30.0 |

### Process Description
The Authority's Application has been Divided into 6 Major Sections. 

#### 1. Dashboard
  * Once the authority has signed in successfully, they are presented with the dashboard screen which is divided into two main sections. 
  * The first being the analytics section. This section contains two charts. 
  * The first is a donut chart which shows a high level view of the user reports in the authority's zone based on the status (approved, submitted, in progress, etc).
  * Next to that is the stacked bar chart which provides a more detailed view of the status, but this time based on severity as well. 
  * The second section on the dashboard is a filterable data table containing details about the various user reports. This datatable has options for sorting, filtering, selecting specific columns, searching, exporting the data as csv and printing the table contents too. 
  * On clicking any report in the datatable, the authority is presented with the option to update it (status and severity). On pressing update they are asked to describe their reason of update in a required custom description box. 
  * Authorities can also comment on the report they clicked on and view all the other details of the report as a user would in their My Complaints screen. 
  * Users are sent notifications through email after any update is made on their report. 

#### 2. Map Region View
  * Another screen in the authority app is the map region view section. Here they can view potholes reported in their region through an interactive map view. 
  * Existing users who have at least one report created can manage the status of their report and add additional comments to it or reply on comments from authorities using this section of the App. 
  * A legend is displayed for helping understand the map better. 
  * Custom markers for potholes with different status values ranging on severity are presented to the auhtority on the map. 
  * Authorities can click on any of the markers to view the information window for it. On pressing the view button in the info window authorities are presented with the view and update detailed report section. 
  * They can update the status and severity directly from this view after clicking the button in the info window. On pressing update they are asked to describe their reason of update in a required custom description box. 
  * Authorities can also comment on the report they clicked on and view all the other details of the report as a user would in their My Complaints screen. 
  * Users are sent notifications through email after any update is made on their report. 
  * Also, there is a street view renderer for the users. 
  * Finally there is an option to toggle on and off a heat map layer which is weighted on the severity of potholes reported in the region. 
  
#### 3. Manage Users
  * This screen presents the authority to manage all active users in their zone through a filterable data table. 
  * The data table contains options to filter, search, sort, select columns. 
  * They can view their basic profile details. 
  * They can update thier status to either blocked or allowed based on their activity too. 
  * Users are sent out email notifications regarding updates in their status everytime an authority makes a change. 
  
#### 4. Profile 
  * This screen contains the basic details (avatar, name, email address of the user) 
  * It also contains the address of the authority. 
  * It is then followed by a counter for reports in the authority's zone with a status of either pending, in progress, approved, completed or cancelled. 
  
#### 5. Sign In Screen 
  * This screen contains the option to login using Google. 
  * This uses Google's OAuth 2.0 GAPI for logging in the user. 
  * This also uses the Unsplash API for generating random backgrounds on the side. (When in desktop mode)
  * The app also uses local storage actively to maintain the session state every time in communication with GAPI. 
  * OAuth2.0 Unsplash Logout Local Storage. 
  * An important point to note is that in the authority's app the ouath api has been linked to a stand alone database to authorize authority log-ins. 
  
#### Note. Features associated with each screen have been mentioned in the Feature Stack Table. 

(Process Diagram Here)

### Instructions to Set-Up the Authority Application
 * Follow the instructions on this page to install nodejs and npm. Once successfully done, proceed to the next steps. 
https://docs.npmjs.com/downloading-and-installing-node-js-and-npm.

 * On your terminal. (You can use Git-Bash if you wish to) 

```
1. git clone https://github.com/nirbhayph/spothole.authority.git
2. cd spothole.authority
3. npm install 
4. Change the API KEY for Google Maps by creating a key from https://developers.google.com/maps/documentation/javascript/get-api-key. 
5. Change the ClientId for Google Oauth from https://developers.google.com/identity/protocols/oauth2.
6. Setup the flask and deep learning app on your machine by following the setup instructions for the backend. 
7. Setup the database according to the instructions provided in the backend application's readme document. 
8. Create at least one user in the authority datatabase before proceeding. 
9. Once your backend is working and you have tested the local apis using a tool like Postman, change the api constants in the utility folder of the authority app's src/component directory
10. Finally, npm start
11. Enjoy using the app. Feel free to make contributions and raise Pull Requests. 
```
 * Visit http://localhost:3000 in your browser to see spothole authority application running.

### Deploying 

The authority's application has been hosted through GitHub pages. Refer the link: https://github.com/gitname/react-gh-pages to create a similar deployment. 

### Future Work
* Parent Authority Section (Admin User)
* In-App Work Order Assignment 
* Worker App 
* Push Notifications 
* Authority Hierarchy Management 
* Permision Level System 
* Extended Analytics Section (Hierarchy Based) 
* Linking Social Platforms (Twitter)
* News Feed 
* Reward System 

### Note 
For developers out there, if you wish to contribute to the project, feel free to do so. Please review the future work section and create pull requests for ideas and thoughts. Once approved, we can follow up with more discussions.  

### License
This project is licensed under the MIT License - see the LICENSE.md file for details

### Developer

#### Nirbhay Pherwani 
* GitHub - @nirbhayph - https://github.com/nirbhayph
* LinkedIn - https://linkedin.com/in/nirbhaypherwani
* Profile - https://nirbhay.me
* Email - pherwani37@gmail.com

### Acknowledgements and Mentions

* @reactjs - https://reactjs.org/
* @material-design-react - https://material-ui.com/
* @react-google-maps - https://www.npmjs.com/package/react-google-maps
* @google-maps-api - https://developers.google.com/maps/documentation/javascript/
* @google-oauth-gapi - https://developers.google.com/identity/protocols/oauth2
* @mui-treasury - https://mui-treasury.com/
* @mui-datatable - https://github.com/gregnb/mui-datatables
* @recharts - http://recharts.org/en-US/
* @axios - https://www.npmjs.com/package/axios
* @dateformat - https://www.npmjs.com/package/dateformat
* @AmericanAutomobileAssociation - https://www.aaa.com/stop/
* @SafetyResourceCenter - https://www.trafficsafetystore.com/blog/the-plague-of-potholes-how-to-save-americas-roadways/
* @loadash - https://lodash.com/
* @create-react-app - https://reactjs.org/docs/create-a-new-react-app.html
* @gh-pages - https://www.npmjs.com/package/gh-pages
* @github - https://github.com
* @roshniw - https://roshniwadhwa.me
* @trello - https://trell.com
* @figma - https://figma.com
* @google-keep - https://keep.google.com
* @npmjs - https://www.npmjs.com
* @imgbb - https://imgbb.com/
* @snap2html - https://www.rlvision.com/snap2html/about.php
