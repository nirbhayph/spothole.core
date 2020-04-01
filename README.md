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
#### The backend comprises of three main sections. The first being the object detection model built using Darkflow. The second being the database for the application. The third being the Flask API for data exchange between the model built, the database and the frontend. 
#### 1. Object Detection Model
  * As the focus of the application was to create a rest api to automate the process of pothole validation with media files, from the beginning itself a cloud server was used for implementation. A [EC2 Amazon Web Services Instance](https://aws.amazon.com/ec2/instance-types/) was used for this purpose. 
  
  * AWS EC2 C5 Instance (model: c5.xlarge) after choosing Ubuntu 18 which features the Intel Xeon Platinum 8000 series and offers a set of 4vCPUs each with 8 GiB of memory was chosen for training the object detection model. Please refer the deployment section to learn more about setting this up. 
  
  * The model is trained on top of [Darkflow](https://github.com/thtrieu/darkflow)  and built on top of pretrained weights which were obtained from [Darknet](https://pjreddie.com/darknet/). 
  
  * For crawling images relevant to our label ‘pothole’, images were crawled using the open source google image search package, along with using the serpapi image search tool.
  
  * In addition to this freely available pothole video feeds to create the dataset were also used. For a near to decent detection result, we should look to collect at least 500+ images. The dataset has been provided with the repository. 
  
  * In case of video files, we can upload it to our server using an sftp client like Filezilla or by directly using ssh on the terminal of our local machine. The next step was to write a script to slice this uploaded video to images. Python’s  OpenCV (cv2 package and Video Capture Module)  to divide the feed into frames. 
  
  * Using ‘pip install’ the following dependencies need to be added. [pillow, lxml, jupyter, matplotlib, protobuffer] 
  
  * After cloning the DarkFlow repository, to prepare the input files for DarkFlow we need to consider two things. Firstly, we need an RGB image which is encoded as jpeg or png and secondly, we need a list of bounding boxes (xmin, ymin, xmax, ymax) for the image and the class of the object in the bounding box. 
  
  * Our class, in this case, is ‘pothole’. We then need to label our images with a tool like LabelImg to identify areas of interest with bounding boxes. 
  
  * LabelImg is a graphical image annotation tool that is written in Python and uses Qt for the graphical interface. 
  
  * It supports Python 2 and 3. The annotations are saved as XML files in the Pascal VOC format We can split the data to train and test sets before running the training command. 
  
  * Now the datasets needed for feeding darkflow package in the required format are available.
  
  * We need to first configure Darkflow by modifying the configuration file and labels.txt file. 
  
  * Then we need to make a copy from cfg/tiny-yolo-voc.cfg and create a cfg/tiny-yolo-voc-1c.cfg file with the same content. Change the line 114 to filters=30 [num * (classes + 5)] and set classes=1 as we have only one class ‘pothole’. 
  
  * In the label.txt file remove all the labels and just keep the pothole label. 
  
  * Once done, refer to the training command on this link. [Train Yolo with Darkflow](https://sites.google.com/view/tensorflow-example-java-api/complete-guide-to-train-yolo/train-yolo-with-darkflow), and start training with the dataset created earlier.
  
  * Using the test sets the model can be verified to check the accuracy of our newly trained object tracking model. This can now also be applied to various snippets of video to highlight the potential of object detection on potholes. Refer to the link mentioned in the above step for the testing command. It also contains options to restart training from a previous checkpoint.
  
  * We will then proceed to saving the built graph as a protobuf file. Read this link on [Darkflow](https://github.com/thtrieu/darkflow#save-the-built-graph-to-a-protobuf-file-pb) to understand this better. 
  ```
  flow --pbLoad built_graph/yolo.pb --metaLoad built_graph/yolo.meta --imgdir sample_img/
  ```
  
  * The dataset, the annotation files, the built model have all been provided with the repository for reference. You can follow the steps mentioned above only if you wish to have a fresh start to training and testing the model. 
  
  (Process Diagram Here) 
  
#### 2. Database
 * The database is comprised of 4 main entities. (Authority, Public User, Reports, Comments). 
 
 * Please refer the database scheme to know more about the attributes associated with each entity. 
 
 * The authority is someone that has the authorization to manage reports in their zone. A zone is specfied as a 1000 mts radius. 
 
 * A public user is someone that can create a report using the citizen app. 
 
 * A report is basically details of a submission that has been validated through the object detection model. 
 
 * Comments are basically communication exchange between an authority and a user on a report. 
 
 * A service layer file in python has been created with different methods which are used by the api to communicate with the database for performing CRUD operations. 
 
#### Schema Diagram 
<img src="https://github.com/nirbhayph/spothole.core/blob/master/mysql_database/spothole_db_schema.png" alt="Schema Diagram">
 
#### 3. Flask API 
 * The Flask API has been built for data exchange between the front end applications, the object detection model and the database. 
 
 * For understanding the front end side of things please refer the important urls section of this read me file. 
 
 * A app controller script has been created to communicate with the service layers (mysql, mail service and parent(object detection))
 
 * The following endpoints have been created for the API. 

| End Point | Screen Name | Method | Params | Application
| --- | --- | --- | --- | --- |
| /api/profile/authority/update | For updating a authority's profile details | POST | Parameters | Authority |
| /api/authority/check | For validating auhtority credentials | POST | Parameters | Authority |
| /api/authority/reports/geonear | For querying reports in an authority's zone | POST | Parameters | Authority |
| /api/authority/update/report | For updating a report's status (for authority) | POST | Parameters | Authority |
| /api/profile/authority/data | For retreiving a authority's profile details, location and address | POST | Parameters | Authority |
| /api/authority/update/user/status | For changing the status of a user (blocked / allowed) | POST | Parameters | Authority |
| /api/authority/send/email | For notifying a user via email | POST | Parameters | Authority | 
| /api/reports/all | For retrieving all users reports | POST | Parameters | Citizen, Authority |
| /api/reports | For retrieveing a particular user's reports | POST | Parameters | Citizen, Authority |
| /api/submit/report/comment | For submitting a comment on a report | POST | Parameters | Citizen, Authority |
| /api/reports/comments | For retrieving all comments on a report | POST | Parameters | Citizen, Authority |
| /api/submit/report | For submitting a new report | POST | Parameters | Citizen |
| /api/upload | For uploading files to the server | POST | Parameters | Citizen |
| /api/detect/single | For detecting whether an image has a pothole. (Object Detection) | POST | Parameters | Citizen |
| /api/profile/update | For updating a user's basic profile details | POST | Parameters | Citizen |
| /api/user/validate | For validating a user's status (allowed / blocked) | POST | Parameters | Citizen |
  
(Complete System Architecture Here) 
  
### Key Features
| Feature Name | App Usage |
| --- | --- |
| Darkflow, Darknet Incorporation | Backend |
| Pothole Detection / Validation (Images, Video) | Citizen |
| Protobuf Compilation (Model) | Backend |
| Image Annotations | Backend |
| Rename and Rearrange Files (Script) | Backend |
| Image Crawler on top of Py Image Search | Backend |
| Video File Slicing (Script) | Backend |
| Output File Storage | Backend | 
| Route 53 (Hosted Zone) on Amazon Web Services (AWS) | Backend | 
| SSL Configuration | Backend |
| Security Groups (AWS) | Backend |
| Media Uploads | Citizen |
| CRUD Operations Authorities Entity | Authority, Citizen |
| CRUD Operations Public Users Entity | Authority, Citizen |
| CRUD Operations Comments Entity | Authority, Citizen |
| CRUD Operations Reports Entity | Authority, Citizen |
| Email Service | Authoritiy |
| Allow / Block User Status | Authority |
| App User Authorization Check | Authority, Citizen |
| Geo Near Reports Querying | Authority |
| Flask API Controller | Authority, Citizen |

### Tools Libraries and Languages Used
* The Backend Application has been built with Python at its Core. 
* The REST API has been built with Flask. 
* The Object Detection Model has been built using DarkFlow on top of Darknet. 
* The Final Model is a Protobuf Compilation (Minified). 
* Mysql has been used for Database needs. 
* Package smptlib has been used for Sending Emails. 
* Package flask_cors has been used to manage Cross Origin Requests. 
* Package mysql is used to interact between Python and MySql. 
* Package cv2 is used to create Bounding Boxes at Runtime.
* The Parent Service which Communicates with the Deep Learning Model uses the TensorFlow Compressed Model created.
* Amazon Web Services has been used for Deployment Purposes. 
* Certbot has been used for HTTPS Configuration
* Freenom has been used for Domain needs.
* Apache is used for Server needs.
* FileZilla and GitBash are used for SFTP and SSH needs. 
* Chrome Dev Tools and Postman are used for API Manual Testing. 

### Instructions to Set-Up the Backend Application 
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

The authority's application has been hosted through Amazon Web Services. To set up the application on a EC2 Instance and a Route 53 Hosted Zone for your choice of Domain Name from a site like Freenom for free refer the following screenshots. 




### Future Work
* Pothole Dimension (Width / Height) Analysis 
* Machine Level Severity Analysis
* OAuth JWT Server Authorization
* Worker App Backend  
* Push Notifications 
* Authority Hierarchy Management (Database, API) 
* Permision Level System (Database, API)
* Analytics API
* Extended Analytics Section (Hierarchy Based)  
* News Feed (Database, API)
* Reward System (Database, API)
* User Blocking (Region Level)

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
