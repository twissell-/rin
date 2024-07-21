# rin

A flask application to handle my webhooks automations

## nginx config

```
    # .apps/nginx/sites-available/default
    location /rin/ {
            proxy_pass         http://127.0.0.1:20464;
            proxy_redirect     off;
            proxy_set_header   Host $host:$server_port;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;
   }
```
