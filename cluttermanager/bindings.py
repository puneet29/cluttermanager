from collections import defaultdict


audio_files = {'aif', 'cda', 'mid', 'midi', 'mp3',
               'm4a', 'mpa', 'ogg', 'wav', 'wma', 'wpl'}

compressed_files = {'7z', 'arj', 'deb',
                    'pkg', 'rar', 'rpm', 'tar.gz', 'z', 'zip'}

disc_files = {'dmg', 'iso', 'toast', 'vcd'}

data_db_files = {'csv', 'dat', 'db', 'dbf',
                 'log', 'mdb', 'sav', 'sql', 'tar', 'xml'}

email_files = {'email', 'eml', 'emix', 'msg', 'oft', 'ost', 'pst', 'vcf'}

executable_files = {'apk', 'bat', 'bin', 'com',
                    'exe', 'gadget', 'jar', 'msi', 'wsf'}

font_files = {'fnt', 'fon', 'otf', 'ttf'}

image_files = {'ai', 'bmp', 'gif', 'ico', 'jpeg',
               'jpg', 'png', 'ps', 'psd', 'svg', 'tif', 'tiff'}

internet_files = {'asp', 'aspx', 'cer', 'cfm', 'cgi', 'css',
                  'htm', 'html', 'js', 'jsp', 'part', 'php', 'rss', 'xhtml'}

presentation_files = {'key', 'odp', 'pps', 'ppt', 'pptx'}

programming_files = {'c', 'cpp', 'class', 'cs', 'py',
                     'h', 'java', 'pl', 'sh', 'swift', 'vb'}

spreadsheet_files = {'ods', 'xls', 'xlsm', 'xlsx'}

system_files = {'bak', 'cab', 'cfg', 'cpl', 'cur', 'dll', 'dmp',
                'drv', 'icns', 'ini', 'lnk', 'sys', 'tmp'}

video_files = {'3g2', '3gp', 'avi', 'flv', 'h264', 'm4v', 'mkv',
               'mov', 'mp4', 'mpg', 'mpeg', 'rm', 'swf', 'vob', 'wmv'}

word_files = {'doc', 'docx', 'md', 'odt',
              'pdf', 'rst', 'rtf', 'tex', 'txt', 'wpd'}

filetypes = {'audio': audio_files, 'compressed': compressed_files,
             'disc': disc_files, 'data': data_db_files,
             'email': email_files, 'executable': executable_files,
             'font': font_files, 'image': image_files,
             'internet': internet_files, 'presentation': presentation_files,
             'programming': programming_files,
             'spreadsheet': spreadsheet_files, 'system': system_files,
             'video': video_files, 'word': word_files}

abstract_types = {'images': image_files, 'audio': audio_files,
                  'video': video_files,
                  'programs': executable_files.union(programming_files),
                  'documents': data_db_files.union(presentation_files).union(
                      spreadsheet_files).union(word_files),
                  'compressed': compressed_files}

extension_to_type = defaultdict(lambda: 'other')

for type_name, extensions in filetypes.items():
    for extension in extensions:
        extension_to_type[extension] = type_name

extension_to_type_abstracted = defaultdict(lambda: 'other')

for type_name, extensions in abstract_types.items():
    for extension in extensions:
        extension_to_type_abstracted[extension] = type_name
