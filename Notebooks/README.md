# Notebooks

Các file `.ipynb` được generate tự động từ thư mục `Programming_Languages/` bằng script `scripts/md_to_notebook.py`.

## Generate Notebooks

```bash
python scripts/md_to_notebook.py
```

## Cài đặt Jupyter Kernel

> **Note:** Nếu chỉ xem notebook trên GitHub hoặc VS Code thì **không cần** cài kernel.

Để **chạy code** trong notebook, cần cài kernel tương ứng:

### Python (có sẵn)

```bash
pip install ipykernel
```

### C — [jupyter-c-kernel](https://github.com/brendan-rius/jupyter-c-kernel)

```bash
pip install jupyter-c-kernel
install_c_kernel
```

### C++ — [xeus-cling](https://github.com/jupyter-xeus/xeus-cling)

```bash
conda install -c conda-forge xeus-cling
```

### Go — [gophernotes](https://github.com/gopherdata/gophernotes)

```bash
go install github.com/gopherdata/gophernotes@latest
mkdir -p ~/.local/share/jupyter/kernels/gophernotes
cp "$(go env GOPATH)/pkg/mod/github.com/gopherdata/gophernotes@*/kernel/*" ~/.local/share/jupyter/kernels/gophernotes/
```

### Java — [IJava](https://github.com/SpencerPark/IJava)

```bash
# Download IJava release từ GitHub
# https://github.com/SpencerPark/IJava/releases
unzip ijava-*.zip -d ijava
cd ijava && python install.py --sys-prefix
```

### JavaScript — [IJavascript](https://github.com/nicklang/ijavascript)

```bash
npm install -g ijavascript
ijsinstall
```

### TypeScript — [tslab](https://github.com/nicklang/ijavascript)

```bash
npm install -g tslab
tslab install
```

### Rust — [evcxr_jupyter](https://github.com/evcxr/evcxr)

```bash
cargo install evcxr_jupyter
evcxr_jupyter --install
```

### PHP — [Jupyter-PHP](https://github.com/Litipk/Jupyter-PHP)

```bash
# Cần PHP >= 7.0 và Composer
composer global require litipk/jupyter-php
jupyter-php-install
```

## Kiểm tra kernel đã cài

```bash
jupyter kernelspec list
```
