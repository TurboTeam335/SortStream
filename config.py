import logging

LOG_LEVEL = logging.INFO

category_mapping = {
    'Documents': ['.doc', '.docx', '.odt', '.rtf', '.tex', '.txt', '.wpd', '.pdf'],
    'Data Files': ['.csv', '.dat', '.key', '.ppt', '.pptx', '.xml'],
    'Audio Files': ['.aif', '.flac', '.m4a', '.mid', '.mp3', '.ogg', '.wma'],
    'Video Files': ['.3gp', '.asf', '.flv', '.m4v', '.mp4', '.mpg', '.srt', '.swf', '.ts', '.vob', '.wmv'],
    '3D Image Files': ['.3dm', '.3ds', '.blend', '.dae', '.fbx', '.max', '.obj'],
    'Raster Image Files': ['.bmp', '.dcm', '.dds', '.djvu', '.gif', '.heic', '.jpg', '.jpeg', '.png', '.psd', '.tga', '.tif'],
    'Vector Image Files': ['.ai', '.cdr', '.emf', '.eps', '.ps', '.svg', '.vsdx'],
    'Page Layout Files': ['.indd', '.oxps', '.pmd', '.pub', '.qxp', '.xps'],
    'Spreadsheet Files': ['.numbers', '.ods', '.xlr', '.xls', '.xlsx'],
    'Database Files': ['.accdb', '.crypt14', '.db', '.mdb', '.odb', '.pdb', '.sqlite'],
    'Executable Files': ['.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.exe', '.gadget', '.jar', '.wsf'],
    'Web': ['.asp', '.html', '.css', '.js', '.php'],
    'Code': ['.c', '.cpp', '.cs', '.java', '.js', '.py', '.rb', '.swift'],
    'Archives': ['.7z', '.rar', '.tar', '.gz', '.zip'],
    'E-books': ['.epub', '.mobi', '.azw']
}

