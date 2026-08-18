# Storage Protocols & Cloud Backend Optics Report

This report analyzes **storage protocols (`gs://`, `s3://`, `abfs://`, etc.) and backend filesystem drivers** across open-source codebases.

---

## 📊 Global Cloud Provider Breakdown

- **Repositories/Targets Scanned:** `13`
- **Total Files Scanned:** `9944`
- **Total Protocol Usages Detected:** `4086`

| Cloud Provider / Backend | Total Usages | % Share |
| :--- | :---: | :---: |
| **Web / HTTP** | **3579** | `87.6%` |
| **Amazon Web Services (S3)** | **337** | `8.2%` |
| **In-Memory Storage** | **41** | `1.0%` |
| **Google Cloud Storage (GCS)** | **40** | `1.0%` |
| **Local Filesystem** | **33** | `0.8%` |
| **Microsoft Azure (Blob/ADLS)** | **26** | `0.6%` |
| **Other / Chained Protocol** | **19** | `0.5%` |
| **Hadoop HDFS** | **11** | `0.3%` |

---

## 📈 Protocol URI Scheme Breakdown

| Protocol Scheme | Occurrences | % Share | Description |
| :--- | :---: | :---: | :--- |
| **`https`** | **3285** | `80.4%` | HTTPS Secure Remote Stream (`https://`) |
| **`s3`** | **337** | `8.2%` | Amazon S3 (`s3://`) |
| **`http`** | **294** | `7.2%` | HTTP Remote Stream (`http://`) |
| **`memory`** | **41** | `1.0%` | In-Memory Filesystem (`memory://`) |
| **`gs`** | **36** | `0.9%` | Google Cloud Storage (`gs://`) |
| **`file`** | **33** | `0.8%` | Local Disk (`file://`) |
| **`abfss`** | **20** | `0.5%` | Azure Data Lake Gen2 (`abfss://`) |
| **`zip`** | **15** | `0.4%` | Zip Archive Chained (`zip://`) |
| **`hdfs`** | **11** | `0.3%` | Hadoop Distributed FS (`hdfs://`) |
| **`gcs`** | **4** | `0.1%` | Google Cloud Storage (`gcs://`) |
| **`azureblob`** | **4** | `0.1%` | Custom protocol (azureblob://) |
| **`abfs`** | **4** | `0.1%` | Azure Blob Storage (`abfs://`) |
| **`az`** | **2** | `0.0%` | Azure Storage (`az://`) |