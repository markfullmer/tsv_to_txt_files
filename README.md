# .tsv to .txt downloader

Given a properly-formatted tab-separated values file with a URL to a transcript file, this will download each row's URL and save it, with headers, to a .txt file.

## Running the script
`python make_text_files.py`


## TSV Format
Each line of the tab-separated file must be in the format:

```
<discipline>	<sub_discipline>	<topic>	<author>	<video_title	<transcript_url>
```

The TSV file should not include a header row.

### Example row in TSV
```
economicsfinancedomain	corefinance	americancalloptions	SalKhan	12739	http://www.khanacademy.org/api/internal/videos/3o82OwR78wU/transcript
```

### Example .txt output
```
<doc discipline="economicsfinancedomain" sub_discipline="corefinance" topic="americancalloptions" author="SalKhan" video_title="12739" transcript_url="http://www.khanacademy.org/api/internal/videos/3o82OwR78wU/transcript">
Voiceover: Here are some option quotes from CNBC.com and my goal here is to really just familiarize you with the quote, so you know what you're looking at...
</doc>
```

