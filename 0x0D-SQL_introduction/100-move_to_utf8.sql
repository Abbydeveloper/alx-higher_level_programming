-- convert hbtn_0c_0 databast to UTF8
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4, collate utf8mb4_unicode_ci;
ALTER first_table CONVERT TO CHARACTER SET utf8mb4, collate utf8mb4_unicode_ci;
