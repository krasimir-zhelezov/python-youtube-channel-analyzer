# YouTube Channel Analyzer

A Python tool that fetches and analyzes video data from YouTube channels using the [YouTube Data API v3](https://developers.google.com/youtube/). Currently supports analysis of up to 50 videos per channel.

## Features

- Fetch video statistics by channel username
- Analyze engagement metrics
- Export data for further processing
- (Future) Data visualization capabilities

## Prerequisites

- Python 3.7+
- YouTube Data API v3 key
- Required Python packages (see Installation)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/youtube-channel-analyzer.git
   cd youtube-channel-analyzer
   ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a .env file in the project root and add your YouTube API key:
    ```env
    API_KEY=your_youtube_api_key_here
    ```

## Usage

```bash
python main.py
```

## TODO
* Rewrite implementation in Rust for performance
* Develop GUI interface
* Add data visualization capabilities
* Increase video limit beyond 50
* Add CSV/Excel export functionality

## Limitations
* Currently limited to analyzing 50 most recent videos per channel

## License
This project is licensed under the **GNU General Public License**.  
See [LICENSE](LICENSE) for the full text.