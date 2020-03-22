# Clutter Manager

**If you are a clumsy guy like me who clutters up their filesystem with all sorts of files, then this tool is for you.**

Clutter Manager sorts all the files inside the folders according to their respective types and makes an Index for all the files for easy searching.

## Usage

1. Install using PyPI

    ```bash
    pip install cluttermanager
    ```

2. Run cluttermanager

    ```bash
    cluttermanager --root <path to any clumsy directory> [--abstract <True/False>] [--undo]
    ```

## Usage [Developer]

1. Clone Directory

    ```bash
    git clone https://github.com/puneet29/cluttermanager.git
    ```

2. Change directory

    ```bash
    cd cluttermanager
    ```

3. Create and activate Virtual Environment

    ```bash
    python3 -m venv venv
    . venv/bin/activate
    ```

4. Install cluttermanager

    ```bash
    python3 setup.py install
    ```

5. Run cluttermanager

    ```bash
    cluttermanager --root <path to any clumsy directory> [--abstract <True/False>] [--undo]
    ```

## TODO

- [x] Initial release

- [x] Abstraction parameter

- [x] Undo clutter

- [x] Make a PyPI package

- [x] Deploy on PyPI

- [ ] Indexing

- [ ] Depth parameter

- [ ] Documentation
