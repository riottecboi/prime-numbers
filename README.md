# Prime Numbers

The python gmpy2 module has a next_prime() function that allows to calculate prime numbers

https://gmpy2.readthedocs.io/en/latest/mpz.html?highlight=next_prime


We will have to install it with `pip3 install gmpy2` but `gmpy2` will not work unless its requirements are installed in ubuntu. The requirements are `libgmp-dev` `libmpfr-dev` and `libmpc-dev`. Please install them with apt install as usual.

`sudo apt-get update`

`sudo apt-get install python-gmpy2` hoặc `sudo apt-get install python3-gmpy2`


Once `gmpy2` is installed read the documentation and try to create that prime generation algorithm.

----------------------------------------------------------------------------------------------------------------------------------------------------

# Số nguyên tố

Python có mô-đun hỗ trợ người dùng tính toán được số nguyên tố tiếp theo bằng số được nhập vào bất kể dữ liệu đầu vào có là số nguyên tố hoặc không.

`gmpy2` sử dụng hàm `next_prime()` để tính toán, có thể tham khảo thêm tại 

https://gmpy2.readthedocs.io/en/latest/mpz.html?highlight=next_prime

Có thể cài đặt bằng trình quản lí thư viện cho Python là `pip` hoặc phần mềm quản lí cài đặt phần mềm trên Linux là `apt`

Cài đặt bằng `apt`:

`sudo apt-get update`

`sudo apt-get install python-gmpy2` hoặc `sudo apt-get install python3-gmpy2`

Cài đặt bằng `pip`:

`pip3 install gmpy2` hoặc `pip install gmpy2`

nhưng cần phải bảo đảm `libgmp-dev` `libmpfr-dev` and `libmpc-dev` đã được cài đặt sẵn 
