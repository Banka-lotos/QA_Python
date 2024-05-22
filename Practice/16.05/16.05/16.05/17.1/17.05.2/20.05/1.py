def analyze_logs(logs):

    ip_to_urls = {}
 
    for log in logs:
        
        ip, url = log.split()
       
        ip_to_urls.setdefault(ip, set()).add(url)

    return {ip: len(urls) for ip, urls in ip_to_urls.items()}

logs = [
    '192.168.0.1 /home',
    '192.168.0.1 /about',
    '192.168.0.2 /home',
    '192.168.0.1 /home',
    '192.168.0.2 /contact',
    '192.168.0.1 /about',
]

print(analyze_logs(logs))

