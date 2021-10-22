

kubectl patch svc proxy-public -n nfs -p '{"spec": {"type": "LoadBalancer", "externalIPs":["192.168.1.1"]}}'



helm uninstall jupyterhub.v.1 -n nfs




helm upgrade --install jupyterhub.v.1 jupyterhub/jupyterhub --namespace nfs --version= 1.1