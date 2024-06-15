# Webcam Monitoring (Thieves Alert)

## Overview

This project implements a webcam monitoring system that detects motion using frame differencing, captures images when motion is detected, and sends an email alert with the captured image attached. The system is designed to provide alerts specifically for detecting potential thieves or intruders.

## Features

- **Motion Detection**: Utilizes frame differencing techniques to detect motion in the webcam feed.
- **Email Alerts**: Sends immediate email notifications with the captured image when motion indicative of a potential theft is detected.
- **Automatic Cleanup**: Periodically cleans up stored images to optimize disk space usage.

## Prerequisites

- Python 3.x
- OpenCV
- Gmail account with app-specific password for sending emails

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/jagadeesh-sagar/Webcam-Monitoring-Thieves-Alert-.git
