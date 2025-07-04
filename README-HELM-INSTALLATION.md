# Helm Chart Installation Guide ⎈

This guide is for customers who want to deploy the application using the provided Helm chart.

## Prerequisites
- Helm 3 installed ([Install Helm](https://helm.sh/docs/intro/install/))
- Access to a Kubernetes cluster (e.g., minikube, kind, EKS, GKE, AKS)
- (Optional) Docker image available in a public registry (e.g., Docker Hub)

## 1. Add the Helm Repository
```bash
helm repo add amitchart https://amithauzer.github.io/helm-phase-3
helm repo update
```

## 2. Install the Chart
### From Published Repository
```bash
helm install my-release amitchart/amitchart \
  --set image.repository=amithauzer/amitchart-phase3-flask \
  --set image.tag=latest
```

### From Local Chart Directory
```bash
helm install my-release ./amitchart \
  --set image.repository=amithauzer/amitchart-phase3-flask \
  --set image.tag=latest
```

## 3. Customize Your Deployment
- Copy `amitchart/values.yaml` to `my-values.yaml` and edit as needed:
  ```bash
  cp amitchart/values.yaml my-values.yaml
  # Edit my-values.yaml
  helm install my-release ./amitchart -f my-values.yaml
  ```
- You can override any value with `--set key=value` on the command line.

## 4. Access the Application
- After installation, follow the output instructions (from `amitchart/templates/NOTES.txt`) to get the service URL. For example:
  ```bash
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services my-release-amitchart)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
  ```

## 5. Upgrade or Uninstall
```bash
helm upgrade my-release ./amitchart -f my-values.yaml
helm uninstall my-release
```

## 6. Troubleshooting
- Check pod and service status:
  ```bash
  kubectl get all
  kubectl describe pod <pod-name>
  kubectl logs <pod-name>
  ```
- Use `helm status my-release` for Helm release info.

---

For advanced configuration, see comments in `values.yaml` and the Helm documentation: https://helm.sh/docs/
