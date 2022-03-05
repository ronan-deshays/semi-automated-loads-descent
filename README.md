# semi-automated-loads-descent
 Semi-automation of manual loads-descent calculations on a simple rectangular project using only Excel formulas as core computing. Some helpers were developped in python to accelerate data preparation for bigger projects.

## Prerequisites
* Python 3.10 and above - [install](https://www.python.org/downloads/)
* Excel 2019 and above - [install](https://www.microsoft.com/microsoft-365/excel)
* excel-formula-parser GitHub project - [install](https://github.com/ronan-deshays/excel-formula-parser) (compatible version already included in this repository)
* Text Editor, like Visual Studio Code - [install](https://code.visualstudio.com/)

## Installation
Simply UnZIP and use different scripts.

## Features
* Automatically search data on elements based on their caracteristics in database given by user.
* Form 2 database approach
* At the end, spreadsheet gives G and Q loads (as described in Eurocodes).

## Usage example
* Fill all required databases.
* Fill main calculation Sheet (all columns which does not contains a GET or CALC prefix in their name).
