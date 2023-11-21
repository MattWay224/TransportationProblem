# Transportation Problem

## 🔗 Requirements
- [Python 3.8 or newer](https://www.python.org/downloads/)

## 🚀 Project Setup
1. Clone the repository
    ```shell
    git clone https://github.com/hestrr/linked-int.git
    ```
2. Go to the project directory
    ```shell
    cd TransportationProblem
    ```
3. Install and use virtualenv (optional):
    ```shell
    pip install virtualenv
    python3 -m venv venv
    ```
   On Windows, run:
    ```shell
    .\venv\Scripts\activate.bat
    ```
   On Unix or MacOS, run:
    ```shell
    source venv/bin/activate
    ```
4. Install the requirements:
    ```shell
    pip install -r requirements.txt
    ```
5. Run program
    ```shell
    python main_transportation.py
    ```
   You will be asked to enter the table for transportation problem in matrix form, as well as Demand and Supply vectors.  
   Columns should be separated from each other by a space, and rows by line breaks.

## 🪲 Run tests
```shell
python -m unittest tests/test_transportation.py
```