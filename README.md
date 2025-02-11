# RedditDataEngineering
Learning Reddit Data Pipeline Engineering | AWS End to End Data Engineering


## Overview

This project is an end-to-end data pipeline that extracts data from Reddit, processes it using ETL (Extract, Transform, Load) techniques, and stores it in AWS services for analysis and visualization. The pipeline is automated using Apache Airflow and integrates multiple AWS services, including S3, Glue, Athena, and Redshift.

## Features

- **Automated Data Pipeline**: Uses Airflow to schedule and manage the workflow.
- **Reddit Data Extraction**: Extracts posts from specified subreddits using the Reddit API.
- **Data Transformation**: Cleans and structures the data using Pandas.
- **AWS S3 Storage**: Stores processed data in S3 buckets.
- **AWS Glue & Athena**: Enables data crawling, schema discovery, and querying.
- **AWS Redshift Integration**: Loads structured data into Redshift for analytics.
- **Data Visualization**: Compatible with BI tools such as Power BI, Tableau, and QuickSight.

## Architecture

```
Reddit API → Airflow DAG → S3 → Glue Crawler → Athena Queries / Redshift Data Warehouse → BI Tools
```

## Technologies Used

- **Python** (ETL scripts, API calls, data processing)
- **Apache Airflow** (Workflow orchestration)
- **AWS S3** (Data storage)
- **AWS Glue** (ETL transformations, schema discovery)
- **AWS Athena** (SQL-based querying)
- **AWS Redshift** (Data warehousing)
- **Docker & Docker Compose** (Containerized environment setup)
- **PostgreSQL & Redis** (Airflow backend and message queue)

## Project Setup

### Prerequisites

- AWS account with access to S3, Glue, Athena, and Redshift
- Reddit API credentials (client ID, secret key, user agent)
- Docker and Docker Compose installed

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/aws-data-engineering-pipeline.git
   cd aws-data-engineering-pipeline
   ```

2. **Set Up Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Update the `.env` file with AWS and Reddit API credentials.

4. **Start Airflow and Dependencies**

   ```bash
   docker-compose up -d --build
   ```

5. **Trigger the Airflow DAG**

   - Open Airflow UI at `http://localhost:8080`
   - Enable and trigger the `reddit_pipeline` DAG

## Pipeline Details

### Data Extraction (Reddit API)

- Fetches posts from specified subreddits using the `praw` library.
- Saves raw data as JSON.

### Data Transformation (Pandas)

- Extracts relevant fields (post ID, title, score, comments, etc.).
- Converts timestamps to human-readable format.
- Cleans data and removes unnecessary fields.

### Data Loading (AWS S3)

- Uploads processed CSV files to an S3 bucket.

### AWS Glue & Athena Integration

- AWS Glue Crawler discovers schema from S3 data.
- Athena queries allow SQL-based exploration of the dataset.

### Data Warehouse (AWS Redshift)

- Redshift cluster stores structured data.
- Data is queried using Redshift Query Editor.


## License

This project is licensed under the MIT License.

### MIT License

```
MIT License

Copyright (c) [Year] [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

