import os
import shutil

basepath = '.'

programming_files = {'.c': 'C', '.h': 'C/C++ header file', '.cpp': 'C++', '.py': 'Python', '.pyc': 'Python', '.cs': 'C#', '.js': 'JavaScript', '.html': 'HTML', '.html': 'HTML',
                     '.m': 'Objective C', '.java': 'Java', '.jav': 'Java', '.php': 'PHP', '.aspx': 'ASP .Net', '.sh': 'Bash Script file', '.vb': 'Visual basic file', '.swift': 'SWIFT',
                     '.css': 'CSS', '.xml': 'XML', '.rb': 'Ruby', '.pl': 'Perl', '.ipynb': 'Jupyter Notebook', '.json': 'Json'}
audio_files = {'.aif': 'AIF', '.midi': 'MIDI', '.mid': 'MIDI', '.mp3': 'MP3', '.mpa': 'MPEG-2', '.ogg': 'Ogg', '.wav': 'WAV', '.wma': 'WMA', '.wpl': 'Windows Media Player playlist'
               }
compressed_files = {'.7z': '7-zip', '.arj': 'ARJ', '.deb': 'Debian Software Package', '.rar': 'RAR', '.pkg': 'Package file', '.rpm': 'Red Hat Package Manager',
                    '.tar.gz': 'Tarball compressed file', '.z': 'Z compressed file', '.zip': 'Zip compressed file', '.tar.bz2': 'tarball compressed'
                    }
disk_image_files = {'.bin': 'Binary disc image', '.dmg': 'macOS X disk image', '.iso': 'ISO disc image', '.vcd': 'Virtual CD', '.toast': 'Toast disc image'
                    }
data_files = {'.csv': 'CSV', '.dat': 'Data file', '.db': 'Database file', '.dbf': 'Database file', '.log': 'Log File',
              '.mdb': 'Microsoft Access database file', '.sav': 'Save file', '.sql': 'SQL Database file', '.tar': 'Linux / Unix tarball file archive'}
executable_files = {'.apk': 'Android package file', '.bat': 'Batch file', '.bin': 'Binary file', '.com': 'MS-DOS command file',
                    '.exe': 'executable file', '.gadget': 'Windows gadget', '.jar': 'Java Archive file', '.wsf': 'Windows Script file', '.appimage': 'App Image'}

image_files = {'.ai': 'Adobe Illustrator', '.bmp': 'Bitmap image', '.gif': 'GIF', '.ico': 'Icon file', '.jpeg': 'JPEG', '.jpg': 'JPEG', '.png': 'PNG', '.ps': 'PostScript file',
               '.psd': 'PSD', '.svg': 'Scalable Vector Graphics file', '.tif': 'TIFF', '.tiff': 'TIFF'
               }
document_files = {'.doc': 'MS-WORD', '.docx': 'MS-WORD', '.odt': 'OpenOffice Writer document file', '.pdf': 'PDF file', '.rtf': 'Rich Text Format',
                  '.tex': 'Latex document file', '.txt': 'Plain text file', '.wks': 'Microsoft Works file', '.wps': 'Microsoft Works file', '.wpd': 'WordPerfect document',
                  '.ods': 'OpenOffice Calc spreadsheet file', '.xlr': 'Microsoft Works spreadsheet file', '.xls': 'Microsoft Excel file', '.xlsx': 'Microsoft Excel Open XML spreadsheet file',
                  '.key': 'Keynote presentation', '.odp': 'OpenOffice Impress presentation file', '.pps': 'PowerPoint slide show', '.ppt': 'PowerPoint presentation',
                  '.pptx': 'PowerPoint Open XML presentation'}
system_files = {'.bak': 'Backup file', '.dll': 'DLL', '.dmp': 'Dump', '.drv': 'Device Driver', '.icns': 'macOS X icon resource file',
                '.msi': 'Windows Installer Package', '.tmp': 'temporary', '.sys': 'Windows system file', '.lnk': 'Windows shortcut', 'cfg': 'Configuration', '.ini': 'Initialization'}

video_files = {'.3gp': '3gp', '.3g2': '3GPP2', '.avi': 'AVI', '.flv': 'Adobe Flash', '.h264': 'H.264', '.m4v': 'Apple MP4', '.mkv': 'MKV', '.mov': 'Apple Quictime movie', '.mp4': 'MPEG4',
               '.mpeg': 'MPEG', '.mpg': 'MPEG', '.rm': 'Real Media', '.swf': 'ShockWave flash', '.vob': 'DVD Video Object', '.wmv': 'Windows Media Video'}


files = [(programming_files, 'Programs'), (audio_files, 'Audios'), (video_files, 'Videos'), (data_files, 'Data'),
         (compressed_files, 'Compressed'), (executable_files,
                                            'Executable'), (image_files, 'Images'), (document_files, 'Documents'),
         (disk_image_files, 'Disk Images'), (system_files, 'System')]

folders = ['Programs', 'Audios', 'Videos', 'Data', 'Executable',
           'Compressed', 'Documents', 'Images', 'Disk Images', 'System', 'Others', 'Folders']

for entry in os.listdir(basepath):
    if os.path.isfile(entry):
        if entry == 'cleanup.py':
            continue
        others = True
        extension = entry.split('.')
        if '.tar.gz' in entry.lower():
            extension[-1] = 'tar.gz'
        elif '.tar.bz2' in entry.lower():
            extension[-1] = 'tar.bz2'

        if len(extension) > 1:
            ext = extension[-1]
            ext = '.' + ext.lower()
        else:
            print(entry, ':', 'others')
            continue
        for file_type in files:
            if ext in file_type[0]:
                others = False
                if not os.path.isdir(file_type[1]):
                    os.makedirs(file_type[1])
                shutil.move(entry, os.path.join(file_type[1], entry))

        if others:
            if not os.path.isdir('Others'):
                os.makedirs('Others')
            shutil.move(entry, os.path.join('Others', entry))
    else:
        if entry in folders:
            continue
        if not os.path.isdir('Folders'):
            os.makedirs('Folders')
        shutil.move(entry, os.path.join('Folders', entry))
