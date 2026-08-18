# Storage Protocols & Cloud Backend Optics Report

This report analyzes **storage protocols (`gs://`, `s3://`, `abfs://`, etc.) and backend filesystem drivers** across open-source codebases.

---

## 📊 Global Cloud Provider Breakdown

- **Repositories/Targets Scanned:** `24`
- **Total Files Scanned:** `9472`
- **Total Protocol Usages Detected:** `4506`

| Cloud Provider / Backend | Total Usages | % Share |
| :--- | :---: | :---: |
| **Web / HTTP** | **3956** | `87.8%` |
| **Amazon Web Services (S3)** | **329** | `7.3%` |
| **Local Filesystem** | **62** | `1.4%` |
| **Google Cloud Storage (GCS)** | **48** | `1.1%` |
| **In-Memory Storage** | **41** | `0.9%` |
| **Microsoft Azure (Blob/ADLS)** | **38** | `0.8%` |
| **Other / Chained Protocol** | **19** | `0.4%` |
| **Hadoop HDFS** | **13** | `0.3%` |

---

## 📈 Protocol URI Scheme Breakdown

| Protocol Scheme | Occurrences | % Share | Description |
| :--- | :---: | :---: | :--- |
| **`https`** | **3730** | `82.8%` | HTTPS Secure Remote Stream (`https://`) |
| **`s3`** | **327** | `7.3%` | Amazon S3 (`s3://`) |
| **`http`** | **226** | `5.0%` | HTTP Remote Stream (`http://`) |
| **`file`** | **62** | `1.4%` | Local Disk (`file://`) |
| **`gs`** | **42** | `0.9%` | Google Cloud Storage (`gs://`) |
| **`memory`** | **41** | `0.9%` | In-Memory Filesystem (`memory://`) |
| **`abfss`** | **19** | `0.4%` | Azure Data Lake Gen2 (`abfss://`) |
| **`zip`** | **15** | `0.3%` | Zip Archive Chained (`zip://`) |
| **`hdfs`** | **13** | `0.3%` | Hadoop Distributed FS (`hdfs://`) |
| **`abfs`** | **11** | `0.2%` | Azure Blob Storage (`abfs://`) |
| **`az`** | **8** | `0.2%` | Azure Storage (`az://`) |
| **`gcs`** | **6** | `0.1%` | Google Cloud Storage (`gcs://`) |
| **`azureblob`** | **4** | `0.1%` | Custom protocol (azureblob://) |
| **`s3a`** | **2** | `0.0%` | Amazon S3A (`s3a://`) |