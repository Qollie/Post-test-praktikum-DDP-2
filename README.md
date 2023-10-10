# Post-test-praktikum-DDP-2

## Flowchart
![Toko hardware komputer](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/a01e4bf5-0c02-417e-a262-df71beab47e6)

## SS Output dan Penjelasan

### Pemilihan role
![pilih role](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/667f7352-cd0c-4ab3-b48a-969fd7e6ffef)

Disini user disuruh memilih role, bisa menjadi admin atau pembeli.

- Jika yang dipilih role admin

  #### Role Admin
  **Login sebagai admin**

  ![Login admin dan menu crud](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/6e5c39fe-08a0-4192-b261-627a90a687fd)

  Jika login benar maka akan muncul menu CRUD untuk admin.

  - **Menu CRUD**

  ![Login admin dan menu crud](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/6e5c39fe-08a0-4192-b261-627a90a687fd)

  Di menu ini terdapat pilihan aksi untuk admin.

    - **Create**

    ![Create](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/1f9dbbdd-67df-43c2-9e9f-cb3ea83d698e)

    Jika admin memilih Nomor 2 maka program akan meminta admin untuk memasukkan nomor, nama, dan harga barang yang ingin dimasukkan ke dalam tabel produk.

    - **Read**

    ![Read](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/674638e0-0c96-430a-87fd-8ada51365421)

    Jika admin memilih nomor 1 maka program akan menampilkan tabel produk yang telah dibuat.

    - **Update**

    ![Update](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/96ef1680-0182-48c6-a562-3f4d1fb60055)

    Jika admin memilih nomor 3 maka program akan meminta nomor produk yang ingin diubah. Jika nomor yang dimasukkan ada dalam tabel, program akan meminta admin untuk memasukkan nama dan harga barang yang baru.

    ![gagal update](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/902e7eb7-9a52-4229-86c5-b4157d98f09e)

    Jika admin memasukkan nomor yang tidak ada dalam tabel, maka program akan memberitahu "Nomor barang tidak ditemukan" dan kembali ke menu CRUD.

    - **Delete**

    ![Delete](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/de55ee44-f010-40d4-a45f-376104da4675)

    Jika admin memilih nomor 4 maka program akan meminta nomor produk yang ingin dihapus.

    - **Exit**

    ![Exit](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/dc2a4ddf-0737-41f6-a470-5ff44cc007f4)

    Jika admin memilih nomor 5 maka program akan berhenti.

- Jika yang dipilih role pembeli

  #### Role Pembeli

  ![beli 1 barang](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/a17f04b4-c6a5-469f-a6cd-30f05529f6d7)

  Program akan menampilkan tabel produk, dan pembeli akan diminta untuk memasukkan nomor produk yang ingin dibeli dan jumlah produk yang ingin dibeli.

  ![Beli 2 barang](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/fd090224-c724-4e7c-9d75-f209417757a0)

  Pembeli juga dapat terus menambahkan barang ke dalam daftar belanja mereka.

  ![Total harga](https://github.com/Qollie/Post-test-praktikum-DDP-2/assets/126032210/087aacc6-437b-4370-b65f-3d3e9375e14e)

  Jika pembeli sudah tidak ingin membeli barang lagi, mereka dapat mengetikkan "000" agar program dapat menampilkan daftar barang yang dibeli dan total harga seluruh belanjaan.
