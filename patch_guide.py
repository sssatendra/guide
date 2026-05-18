import os
import re

html_path = "docker-k8s-guide.html"

# Load current HTML content
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Define the 10-chapter modules array in JavaScript format
new_modules_js = """// ── DATA DEFINITION ──
    const modules = [
      {
        id: 1,
        title: "Zero-to-One Installation & Sandbox Setup",
        category: "docker",
        level: "Fundamentals",
        difficulty: "Beginner",
        tldr: "Build a solid foundation. Get Docker Desktop, WSL2 virtual machines, Kind, Minikube, and the kubectl CLI fully installed, configured, and verified.",
        def: "Before writing Dockerfiles or deploying pods, you must set up your container sandbox. This chapter covers installing the <strong>Docker Engine</strong> on Windows (via WSL2 virtual network bridges), macOS (via Homebrew), and Linux. We then spin up a local Kubernetes cluster using <strong>Kind (Kubernetes-in-Docker)</strong> and <strong>Minikube</strong>, configuring the <strong>kubectl CLI</strong> to control the cluster resources securely.",
        diagram: `
+-----------------------------------------------------------------+
|                       DEVELOPER WORKSTATION                     |
+-----------------------------------------------------------------+
|  [ macOS (Brew) ]     [ Windows (WSL2 Backend) ]    [ Ubuntu ]  |
|         |                        |                       |      |
|         v                        v                       v      |
|  +--------------+        +---------------+        +----------+  |
|  |Docker Engine |        | WSL2 VM Layer |        |Docker-CE |  |
|  +--------------+        +---------------+        +----------+  |
|                                  |                              |
|                                  v                              |
|                    +---------------------------+                |
|                    | Kind Nodes (Run as Pods)  |                |
|                    +---------------------------+                |
|                                  ^                              |
|                                  | (HTTPS port 6443)            |
|                    +---------------------------+                |
|                    |     Kubectl Context       |                |
|                    +---------------------------+                |
+-----------------------------------------------------------------+
        `,
        cards: [
          {
            title: "Docker Desktop & WSL2",
            desc: "Windows Subsystem for Linux (WSL2) allows Docker to run bare-metal Linux containers with near-native performance inside Windows, bypassing slow legacy VM hypervisors."
          },
          {
            title: "Kind & Minikube Engines",
            desc: "Kind boots Kubernetes nodes inside lightweight Docker containers in seconds. Minikube manages a VM-based single-node cluster, providing direct hypervisor access."
          },
          {
            title: "Kubectl CLI Contexts",
            desc: "The admin CLI. Connects securely to the Kubernetes API-Server. Uses ~/.kube/config to map credentials, client certificate paths, and namespaces."
          }
        ],
        tabs: [
          {
            name: "install-docker.sh",
            code: `<span class="c-comment"># --- INSTALLING DOCKER ON UBUNTU / DEBIAN ---</span>
<span class="c-comment"># 1. Update package index and install certificates</span>
sudo apt-get update && sudo apt-get install -y ca-certificates curl gnupg

<span class="c-comment"># 2. Add Docker's official GPG key</span>
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

<span class="c-comment"># 3. Set up the stable repository</span>
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

<span class="c-comment"># 4. Install Docker Engine</span>
sudo apt-get update && sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

<span class="c-comment"># 5. Start and enable Docker service</span>
sudo systemctl enable --now docker
sudo usermod -aG docker $USER

<span class="c-comment"># --- INSTALLING ON MACOS (via Homebrew) ---</span>
brew install --cask docker

<span class="c-comment"># --- VERIFY WSL2 SYSTEM STATUS (Windows PowerShell) ---</span>
wsl --status
wsl --list --verbose`
          },
          {
            name: "boot-k8s.sh",
            code: `<span class="c-comment"># --- BOOTING KUBERNETES VIA KIND ---</span>
<span class="c-comment"># 1. Install Kind CLI (macOS / Linux via Brew)</span>
brew install kind

<span class="c-comment"># 2. Create a Kind multi-node configuration</span>
cat <<EOF > kind-config.yaml
<span class="c-k8s-key">kind</span>: <span class="c-string">Cluster</span>
<span class="c-k8s-key">apiVersion</span>: <span class="c-string">kind.x-k8s.io/v1alpha4</span>
<span class="c-k8s-key">nodes</span>:
- <span class="c-k8s-key">role</span>: <span class="c-string">control-plane</span>
- <span class="c-k8s-key">role</span>: <span class="c-string">worker</span>
- <span class="c-k8s-key">role</span>: <span class="c-string">worker</span>
EOF

<span class="c-comment"># 3. Spin up the cluster</span>
kind create cluster --name dev-cluster --config kind-config.yaml

<span class="c-comment"># --- BOOTING KUBERNETES VIA MINIKUBE ---</span>
minikube start --driver=docker --addons=ingress,dashboard`
          },
          {
            name: "verify-env.sh",
            code: `<span class="c-comment"># 1. Verify Docker CLI can speak to host daemon socket</span>
docker info

<span class="c-comment"># 2. Verify Kubectl context points to the local cluster</span>
kubectl config current-context
kubectl cluster-info

<span class="c-comment"># 3. Check physical nodes are registered and ready</span>
kubectl get nodes -o wide

<span class="c-comment"># Expected Output:</span>
<span class="c-comment"># NAME                         STATUS   ROLES           AGE   VERSION</span>
<span class="c-comment"># dev-cluster-control-plane    Ready    control-plane   45s   v1.28.2</span>
<span class="c-comment"># dev-cluster-worker           Ready    <none>          32s   v1.28.2</span>
<span class="c-comment"># dev-cluster-worker2          Ready    <none>          30s   v1.28.2</span>`
          }
        ],
        commands: [
          { cmd: "docker --version", desc: "Verifies the local Docker engine client and runtime compilation versions." },
          { cmd: "kubectl cluster-info", desc: "Queries the active cluster context to confirm control plane and DNS components respond." },
          { cmd: "kind create cluster --name dev-cluster", desc: "Spins up a complete multi-node Kubernetes cluster inside local Docker runners." }
        ],
        caseStudy: "<strong>Resolving WSL2 VPN Conflicts:</strong> In company VPN setups, you may suffer DNS timeout errors inside WSL2. This is caused by network interface MTU mismatch. Solve this by overriding the default network MTU inside the `/etc/docker/daemon.json` configuration file, settings: `{\\"mtu\\": 1400}`, and executing a clean Docker daemon restart."
      },
      {
        id: 2,
        title: "Docker Core Architecture & Linux Internals",
        category: "docker",
        level: "Fundamentals",
        difficulty: "Intermediate",
        tldr: "Containers are not virtual machines. They are isolated, sandboxed Linux processes running directly on the host operating system's kernel, achieved via namespaces, cgroups, and OverlayFS layers.",
        def: "At the heart of containerization lies the <strong>Linux Kernel</strong>. Docker utilizes kernel namespaces to partition host resources so that a containerized process sees its own isolated view, cgroups to restrict CPU, memory, and I/O usage, and a union filesystem to compose layered copy-on-write image layers into a single cohesive runtime environment.",
        diagram: `
+-------------------------------------------------------------+
|                      APPLICATION PROCESS                    |
+-------------------------------------------------------------+
|  NAMESPACES (Isolation)   |     CGROUPS (Constraints)       |
|  - PID  : Isolated PIDs   |     - CPU    : Shares/Limits    |
|  - NET  : Virtual NICs    |     - Memory : Max Limits/Swap  |
|  - MNT  : Custom Mounts   |     - I/O    : Read/Write IOPS  |
|  - USER : Root Remapping  |     - PIDs   : Fork-Bomb Guard  |
+---------------------------+---------------------------------+
|                       UNION FILESYSTEM                      |
|  - Base Image Layer (Read-Only)                             |
|  - Intermediate Dependency Layers (Read-Only)               |
|  - Container Thin Layer (Read-Write - Copy-on-Write)        |
+-------------------------------------------------------------+
|                      HOST LINUX KERNEL                      |
+-------------------------------------------------------------+
        `,
        cards: [
          {
            title: "Namespaces (Isolation)",
            desc: "Provides processes with their own system resources. E.g., PID namespace isolates the process ID space, NET namespace isolates network cards/ports, and MNT namespace isolates custom filesystem mount points."
          },
          {
            title: "Control Groups (cgroups)",
            desc: "Enforces strict boundaries on hardware resources. Prevents a single rogue container from consuming 100% of the host's memory (OOM crash) or CPU cores, ensuring multi-tenant reliability."
          },
          {
            title: "OverlayFS (Layered Storage)",
            desc: "A Union Filesystem that mounts multiple directories onto a unified view. It features a read-only 'lowerdir' (image layers) and a read-write 'upperdir' (container runtime data), leveraging copy-on-write."
          }
        ],
        tabs: [
          {
            name: "inspect-layer.sh",
            code: `<span class="c-comment"># 1. Spin up a lightweight Nginx container</span>
docker run -d --name web-server -p 8080:80 nginx:alpine

<span class="c-comment"># 2. Inspect the low-level overlay filesystem directory configuration</span>
docker inspect web-server | grep -A 10 "GraphDriver"

<span class="c-comment"># Expected Output:</span>
<span class="c-comment"># "GraphDriver": {</span>
<span class="c-comment">#     "Data": {</span>
<span class="c-comment">#         "LowerDir": "/var/lib/docker/overlay2/&lt;hash-lower&gt;/diff",</span>
<span class="c-comment">#         "MergedDir": "/var/lib/docker/overlay2/&lt;hash-merged&gt;/merged",</span>
<span class="c-comment">#         "UpperDir": "/var/lib/docker/overlay2/&lt;hash-upper&gt;/diff",</span>
<span class="c-comment">#         "WorkDir": "/var/lib/docker/overlay2/&lt;hash-work&gt;/work"</span>
<span class="c-comment">#     },</span>
<span class="c-comment">#     "Name": "overlay2"</span>
<span class="c-comment"># }</span>

<span class="c-comment"># 3. View running container namespaces on the host system</span>
lsns -t pid`
          },
          {
            name: "cgroup-limits.sh",
            code: `<span class="c-comment"># Run a stress-testing container with strict cgroup memory and CPU limits</span>
docker run --name stress-app \\
  --cpus="1.5" \\
  --memory="512m" \\
  --memory-swap="1g" \\
  -d progrium/stress --cpu 2 --io 1 --vm 2 --vm-bytes 128M

<span class="c-comment"># Inspect the live cgroups directory on a system running systemd/cgroups v2</span>
cat /sys/fs/cgroup/system.slice/docker-&lt;container-long-id&gt;.scope/memory.max

<span class="c-comment"># Expected output (in bytes):</span>
<span class="c-comment"># 536870912  (which equals 512MB)</span>`
          },
          {
            name: "overlayfs-explore.sh",
            code: `<span class="c-comment"># Examine OverlayFS on host storage directory</span>
sudo ls -lah /var/lib/docker/overlay2/

<span class="c-comment"># When a file inside the container is modified, the engine:</span>
<span class="c-comment"># 1. Searches lowerdir for the target file</span>
<span class="c-comment"># 2. Copies the target file up to the read-write upperdir layer (Copy-On-Write)</span>
<span class="c-comment"># 3. Modifies the copied file in upperdir. MergedDir reflects this update instantly.</span>`
          }
        ],
        commands: [
          { cmd: "docker inspect web-server", desc: "Retrieves complete, low-level JSON metadata of a container, showing networks, ports, and OverlayFS paths." },
          { cmd: "lsns -t pid", desc: "Lists all process ID namespaces active on the host machine kernel." },
          { cmd: "docker stats", desc: "Provides a live, real-time resource usage stream of active containers (CPU, memory, net I/O, disk I/O)." }
        ],
        caseStudy: "<strong>VMs vs Containers:</strong> A Virtual Machine includes the application, required binaries, libraries, and an entire guest OS, which occupies gigabytes and takes minutes to boot because of hardware virtualization. A container shares the host OS kernel and isolates guest resources, booting in milliseconds, taking only megabytes, and running at near-native bare-metal speed."
      },
      {
        id: 3,
        title: "Secure, Multi-Stage Production Dockerfiles",
        category: "docker",
        level: "Advanced",
        difficulty: "Expert",
        tldr: "Writing production Dockerfiles demands a secure mindset. Utilize multi-stage builds, non-root users, strict caching layers, and minimal distroless/alpine base images to reduce vulnerability footprints.",
        def: "Every instruction in a Dockerfile adds a read-only filesystem layer. By grouping commands intelligently, excluding unnecessary files using <code>.dockerignore</code>, deploying multi-stage pipelines to compile assets, and running under unprivileged user privileges, you craft slim, secure, high-performance images optimized for cloud runners.",
        diagram: `
+-------------------------------------------------------------+
|                 STAGE 1: BUILD & DEPS (Heavy)               |
+-------------------------------------------------------------+
|  - Node:20-alpine (Source Image)                            |
|  - Copy Package files -> RUN npm install (Installs devDeps) |
|  - Copy App Source    -> RUN npm run build (Compiles TS)    |
+-------------------------------------------------------------+
                               |
                               |  Only copy built assets
                               v
+-------------------------------------------------------------+
|                STAGE 2: PRODUCTION RUNNER (Slim)            |
+-------------------------------------------------------------+
|  - Node:20-alpine (Minimal base)                            |
|  - Copy /dist from STAGE 1                                  |
|  - Copy node_modules (production dependencies only)         |
|  - Create unprivileged USER node                            |
|  - Entrypoint: ["node", "dist/main.js"]                     |
+-------------------------------------------------------------+
        `,
        cards: [
          {
            title: "Multi-Stage Pipeline",
            desc: "De-couples builders (compilers, SDKs, devDependencies) from runners. Captures only runtime artifacts, cutting image size from 1.2GB down to 60MB."
          },
          {
            title: "Layer Cache Strategy",
            desc: "Copy configuration manifest files (package.json, go.mod) and install dependencies BEFORE copying source code. This keeps dependency layers cached unless packages change."
          },
          {
            title: "Unprivileged User Isolation",
            desc: "By default, containers execute as 'root'. Adding custom USER directives restricts standard exploits by ensuring processes run without administrative privileges inside the host namespace."
          }
        ],
        tabs: [
          {
            name: "Node-TypeScript.Dockerfile",
            code: `<span class="c-comment"># Stage 1: Build & Compile</span>
<span class="c-docker-inst">FROM</span> node:20-alpine <span class="c-docker-inst">AS</span> builder
<span class="c-docker-inst">WORKDIR</span> /usr/src/app
<span class="c-docker-inst">COPY</span> package*.json ./
<span class="c-docker-inst">RUN</span> npm ci
<span class="c-docker-inst">COPY</span> . .
<span class="c-docker-inst">RUN</span> npm run build
<span class="c-docker-inst">RUN</span> npm prune --production

<span class="c-comment"># Stage 2: Minimal Runtime</span>
<span class="c-docker-inst">FROM</span> node:20-alpine
<span class="c-docker-inst">WORKDIR</span> /usr/src/app
<span class="c-docker-inst">COPY</span> --from=builder /usr/src/app/package*.json ./
<span class="c-docker-inst">COPY</span> --from=builder /usr/src/app/node_modules ./node_modules
<span class="c-docker-inst">COPY</span> --from=builder /usr/src/app/dist ./dist

<span class="c-docker-inst">USER</span> node
<span class="c-docker-inst">ENV</span> NODE_ENV=production
<span class="c-docker-inst">EXPOSE</span> 3000
<span class="c-docker-inst">HEALTHCHECK</span> --interval=30s --timeout=5s --start-period=5s --retries=3 \\
  <span class="c-docker-inst">CMD</span> node -e "require('http').request({host: 'localhost', port: 3000, path: '/health'}, (r) => { if (r.statusCode === 200) process.exit(0); else process.exit(1); }).end()"
<span class="c-docker-inst">ENTRYPOINT</span> ["node", "dist/main.js"]`
          },
          {
            name: "Go-Distroless.Dockerfile",
            code: `<span class="c-comment"># Stage 1: Compiler</span>
<span class="c-docker-inst">FROM</span> golang:1.21-alpine <span class="c-docker-inst">AS</span> builder
<span class="c-docker-inst">WORKDIR</span> /app
<span class="c-docker-inst">COPY</span> go.mod go.sum ./
<span class="c-docker-inst">RUN</span> go mod download
<span class="c-docker-inst">COPY</span> . .
<span class="c-docker-inst">RUN</span> CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o server .

<span class="c-comment"># Stage 2: Distroless debian container (Zero Shell access, absolute security)</span>
<span class="c-docker-inst">FROM</span> gcr.io/distroless/static-debian12
<span class="c-docker-inst">COPY</span> --from=builder /app/server /server
<span class="c-docker-inst">USER</span> 65534:65534
<span class="c-docker-inst">EXPOSE</span> 8080
<span class="c-docker-inst">ENTRYPOINT</span> ["/server"]`
          },
          {
            name: "FastAPI-Python.Dockerfile",
            code: `<span class="c-comment"># Stage 1: Setup virtual environment</span>
<span class="c-docker-inst">FROM</span> python:3.11-alpine <span class="c-docker-inst">AS</span> builder
<span class="c-docker-inst">WORKDIR</span> /app
<span class="c-docker-inst">RUN</span> pip install --no-cache-dir virtualenv && virtualenv /venv
<span class="c-docker-inst">ENV</span> PATH="/venv/bin:$PATH"
<span class="c-docker-inst">COPY</span> requirements.txt ./
<span class="c-docker-inst">RUN</span> pip install -r requirements.txt

<span class="c-comment"># Stage 2: Deploy python virtual env to slim runtime</span>
<span class="c-docker-inst">FROM</span> python:3.11-alpine
<span class="c-docker-inst">WORKDIR</span> /app
<span class="c-docker-inst">COPY</span> --from=builder /venv /venv
<span class="c-docker-inst">COPY</span> . .
<span class="c-docker-inst">ENV</span> PATH="/venv/bin:$PATH" \\
    PYTHONUNBUFFERED=1
<span class="c-docker-inst">RUN</span> adduser -D myuser
<span class="c-docker-inst">USER</span> myuser
<span class="c-docker-inst">EXPOSE</span> 8000
<span class="c-docker-inst">ENTRYPOINT</span> ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]`
          }
        ],
        commands: [
          { cmd: "docker build --no-cache -t app:latest .", desc: "Builds a Docker image ignoring cached layers to guarantee fresh downloads and builds." },
          { cmd: "docker history app:latest", desc: "Reveals the layer stack details, instruction origins, and size contributed by each line of the Dockerfile." },
          { cmd: "trivy image app:latest", desc: "Triggers a full security vulnerability scan of the image layer libraries and binary files." }
        ],
        caseStudy: "<strong>Real-world Cache Invalidation:</strong> If you COPY source code before running `npm install`, a single character edit in a file invalidates the cache for all subsequent lines. Placing `COPY package*.json` and `RUN npm install` *first* guarantees that expensive library downloads are cached unless you alter your package manifests."
      },
      {
        id: 4,
        title: "Local Orchestration with Docker Compose",
        category: "docker",
        level: "Intermediate",
        difficulty: "Intermediate",
        tldr: "Declarative orchestration for multi-container applications on a single host. Automates network bridging, persistent volumes, environment management, and dependency ordering.",
        def: "For complex microservice applications, executing individual <code>docker run</code> commands manually is unsustainable. Docker Compose lets you define your entire stack—services, networks, volumes, database passwords, and dependencies—in a single declarative <code>docker-compose.yml</code> file, spin it up with one command, and configure isolated local networks with automatic service discovery.",
        diagram: `
+-------------------------------------------------------------+
|                     ISOLATED COMPOSE NETWORK                |
+-------------------------------------------------------------+
|  +--------------------+             +--------------------+  |
|  |    frontend-web    |   http://   |      backend-api   |  |
|  |    (Port 80)       |------------>|      (Port 5000)   |  |
|  +--------------------+  dns resolve+--------------------+  |
|                                              |              |
|                                              | tcp://       |
|                                              v              |
|  +--------------------+             +--------------------+  |
|  |     redis-cache    |             |    postgres-db     |  |
|  |     (Port 6379)    |             |    (Port 5432)     |  |
|  +--------------------+             +--------------------+  |
+-------------------------------------------------------------+
        `,
        cards: [
          {
            title: "Service Discovery",
            desc: "Every service is assigned a DNS entry matching its service name on the default bridge network. E.g. the backend app connects to the database via 'postgres://postgres-db:5432' instead of an IP address."
          },
          {
            title: "Bind Mounts vs Volumes",
            desc: "Named Volumes ('pg-data') are managed internally by Docker and persist data beyond container lifecycle. Bind Mounts ('./src') map host directories into the container, perfect for live local code reloading."
          },
          {
            title: "Dependency Control",
            desc: "Using 'depends_on' ensures that application boot sequences occur in logical order, utilizing healthchecks to wait until target services are fully initialized, not just started."
          }
        ],
        tabs: [
          {
            name: "docker-compose.yml",
            code: `<span class="c-k8s-key">version</span>: <span class="c-string">"3.8"</span>

<span class="c-k8s-key">services</span>:
  <span class="c-k8s-key">postgres-db</span>:
    <span class="c-k8s-key">image</span>: <span class="c-string">postgres:15-alpine</span>
    <span class="c-k8s-key">container_name</span>: <span class="c-string">production-db</span>
    <span class="c-k8s-key">environment</span>:
      <span class="c-k8s-key">POSTGRES_USER</span>: <span class="c-string">dbadmin</span>
      <span class="c-k8s-key">POSTGRES_PASSWORD</span>: <span class="c-string">secureVault991</span>
      <span class="c-k8s-key">POSTGRES_DB</span>: <span class="c-string">user_ledger</span>
    <span class="c-k8s-key">volumes</span>:
      - <span class="c-string">pg-data:/var/lib/postgresql/data</span>
    <span class="c-k8s-key">networks</span>:
      - <span class="c-string">db-network</span>
    <span class="c-k8s-key">healthcheck</span>:
      <span class="c-k8s-key">test</span>: [<span class="c-string">"CMD-SHELL"</span>, <span class="c-string">"pg_isready -U dbadmin -d user_ledger"</span>]
      <span class="c-k8s-key">interval</span>: <span class="c-number">5s</span>
      <span class="c-k8s-key">timeout</span>: <span class="c-number">5s</span>
      <span class="c-k8s-key">retries</span>: <span class="c-number">5</span>

  <span class="c-k8s-key">backend-api</span>:
    <span class="c-k8s-key">build</span>:
      <span class="c-k8s-key">context</span>: <span class="c-string">.</span>
      <span class="c-k8s-key">dockerfile</span>: <span class="c-string">Dockerfile</span>
    <span class="c-k8s-key">environment</span>:
      <span class="c-k8s-key">DATABASE_URL</span>: <span class="c-string">"postgres://dbadmin:secureVault991@postgres-db:5432/user_ledger"</span>
      <span class="c-k8s-key">REDIS_HOST</span>: <span class="c-string">"redis-cache"</span>
    <span class="c-k8s-key">ports</span>:
      - <span class="c-string">"5000:3000"</span>
    <span class="c-k8s-key">networks</span>:
      - <span class="c-string">db-network</span>
      - <span class="c-string">web-network</span>
    <span class="c-k8s-key">depends_on</span>:
      <span class="c-k8s-key">postgres-db</span>:
        <span class="c-k8s-key">condition</span>: <span class="c-string">service_healthy</span>

  <span class="c-k8s-key">redis-cache</span>:
    <span class="c-k8s-key">image</span>: <span class="c-string">redis:7-alpine</span>
    <span class="c-k8s-key">networks</span>:
      - <span class="c-string">db-network</span>

<span class="c-volumes-key">volumes</span>:
  <span class="c-k8s-key">pg-data</span>:
    <span class="c-k8s-key">driver</span>: <span class="c-string">local</span>

<span class="c-networks-key">networks</span>:
  <span class="c-k8s-key">db-network</span>:
    <span class="c-k8s-key">internal</span>: <span class="c-number">true</span> <span class="c-comment"># Restricts DB network strictly inside docker host</span>
  <span class="c-k8s-key">web-network</span>: {}`
          },
          {
            name: "env-configuration",
            code: `<span class="c-comment"># Declare env variables configuration default file (.env)</span>
PORT=3000
DB_HOST=postgres-db
DB_NAME=user_ledger
DB_USER=dbadmin
DB_PASS=secureVault991
REDIS_HOST=redis-cache

<span class="c-comment"># In Docker Compose, bind variables dynamically:</span>
<span class="c-comment"># environment:</span>
<span class="c-comment">#   - PORT=\${PORT}</span>
<span class="c-comment">#   - DATABASE_URL=postgres://\${DB_USER}:\${DB_PASS}@\${DB_HOST}:5432/\${DB_NAME}</span>`
          },
          {
            name: "local-dev-workflow.sh",
            code: `<span class="c-comment"># Start the stack using specific env file override</span>
docker compose --env-file .env.development up -d

<span class="c-comment"># Spin up and scale the backend-api service instances dynamically</span>
docker compose up -d --scale backend-api=3

<span class="c-comment"># View merged logs from all containers actively running</span>
docker compose logs -f --tail=50`
          }
        ],
        commands: [
          { cmd: "docker compose up -d", desc: "Builds, creates, starts, and attaches containers for all services in background mode." },
          { cmd: "docker compose ps", desc: "Lists all local services, their current status, exit codes, and exposed port mappings." },
          { cmd: "docker compose down -v", desc: "Stops containers, deletes the bridged networks, and wipes out all persistent named volumes." }
        ],
        caseStudy: "<strong>Network Isolation Case Study:</strong> In the configuration above, the `postgres-db` and `redis-cache` are isolated on `db-network`, marked as `internal`. The host machine cannot directly query the database. Only the `backend-api` (which bridges both networks) can route traffic outside the docker network, preventing external hackers from directly targeting port 5432."
      },
      {
        id: 5,
        title: "Small-to-Medium Project - E-Commerce API Stack",
        category: "docker",
        level: "Project Walkthrough",
        difficulty: "Intermediate",
        tldr: "Synthesize Docker concepts. Develop, containerize, and connect a multi-tier local stack incorporating a React front-end, Node.js API, Redis caching, and persistent Postgres storage.",
        def: "This capstone Docker project walks through dockerizing and orchestrating a complete e-commerce API application stack. We write individual Dockerfiles for our React SPA and Node.js gateway server, set up persistent volumes for Postgres data, build high-speed Redis caches, and bind-mount source code directories so that edits on the host sync immediately into active runners without manual compile reloads.",
        diagram: `
 +-----------------------------------------------------------------------+
 |                     E-COMMERCE SYSTEM STRUCTURE                       |
 +-----------------------------------------------------------------------+
 | [ React Web Client ]  -->  Port 3000 mapping (Host Gateway)           |
 |         |                                                             |
 |         v (HTTPS REST API /products)                                  |
 | [ Node.js Express API Server ]  -->  Port 5000 (Internal Bridge)      |
 |         |                                                             |
 |         +----------------------+----------------------+               |
 |         | (Session Store)      | (Structured Data)    |               |
 |         v                      v                      v               |
 |  [ Redis Cache ]        [ Postgres Catalog ]   [ pg-volume ]          |
 +-----------------------------------------------------------------------+
        `,
        cards: [
          {
            title: "Multi-directory Bind Mounts",
            desc: "Binds client/ and server/ code paths on your local drive directly into container running directories, enabling rapid UI updates."
          },
          {
            title: "Live Hot-Reloading Loop",
            desc: "Pipes filesystems modifications automatically via nodemon inside Node, and Vite dev-server HMR inside the web client, ensuring changes reflect on screen instantly."
          },
          {
            title: "Postgres Database Seeding",
            desc: "Utilizes entrypoint scripts inside '/docker-entrypoint-initdb.d' to automatically create schema tables and seed product items upon first database initialization."
          }
        ],
        tabs: [
          {
            name: "directory-structure.txt",
            code: `my-ecommerce-app/
├── docker-compose.dev.yml
├── .env.dev
├── client/
│   ├── Dockerfile.dev
│   ├── package.json
│   ├── vite.config.js
│   └── src/
├── api-server/
│   ├── Dockerfile.dev
│   ├── package.json
│   ├── server.js
│   └── src/
└── db-init/
    └── seed-catalog.sql`
          },
          {
            name: "api-server.js",
            code: `const express = require('express');
const { Pool } = require('pg');
const redis = require('redis');

const app = express();
const pool = new Pool({ connectionString: process.env.DATABASE_URL });
const redisClient = redis.createClient({ url: \`redis://\${process.env.REDIS_HOST}:6379\` });

<span class="c-comment">// API endpoint fetching products with cache fallback</span>
app.get('/products', async (req, res) => {
  try {
    const cachedProducts = await redisClient.get('products');
    if (cachedProducts) return res.json(JSON.parse(cachedProducts));

    const { rows } = await pool.query('SELECT * FROM products');
    await redisClient.setEx('products', 300, JSON.stringify(rows));
    res.json(rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(5000, () => console.log('API Running on port 5000'));`
          },
          {
            name: "docker-compose.dev.yml",
            code: `<span class="c-k8s-key">version</span>: <span class="c-string">"3.8"</span>
<span class="c-k8s-key">services</span>:
  <span class="c-k8s-key">api-server</span>:
    <span class="c-k8s-key">build</span>:
      <span class="c-k8s-key">context</span>: ./api-server
      <span class="c-k8s-key">dockerfile</span>: Dockerfile.dev
    <span class="c-k8s-key">volumes</span>:
      - <span class="c-string">./api-server:/app</span>
      - <span class="c-string">/app/node_modules</span> <span class="c-comment"># Prevent host overwrite</span>
    <span class="c-k8s-key">ports</span>:
      - <span class="c-string">"5000:5000"</span>
    <span class="c-k8s-key">environment</span>:
      - <span class="c-string">DATABASE_URL=postgres://admin:secret@shop-db:5432/catalog</span>
      - <span class="c-string">REDIS_HOST=shop-cache</span>
    <span class="c-k8s-key">depends_on</span>:
      <span class="c-k8s-key">shop-db</span>:
        <span class="c-k8s-key">condition</span>: <span class="c-string">service_healthy</span>

  <span class="c-k8s-key">shop-db</span>:
    <span class="c-k8s-key">image</span>: <span class="c-string">postgres:15-alpine</span>
    <span class="c-k8s-key">environment</span>:
      - <span class="c-string">POSTGRES_USER=admin</span>
      - <span class="c-string">POSTGRES_PASSWORD=secret</span>
      - <span class="c-string">POSTGRES_DB=catalog</span>
    <span class="c-k8s-key">volumes</span>:
      - <span class="c-string">shop-data:/var/lib/postgresql/data</span>
      - <span class="c-string">./db-init:/docker-entrypoint-initdb.d</span> <span class="c-comment"># Seed DB</span>
    <span class="c-k8s-key">healthcheck</span>:
      <span class="c-k8s-key">test</span>: [<span class="c-string">"CMD-SHELL"</span>, <span class="c-string">"pg_isready -U admin -d catalog"</span>]
      <span class="c-k8s-key">interval</span>: <span class="c-number">3s</span>
      <span class="c-k8s-key">timeout</span>: <span class="c-number">3s</span>
      <span class="c-k8s-key">retries</span>: <span class="c-number">3</span>

<span class="c-volumes-key">volumes</span>:
  <span class="c-k8s-key">shop-data</span>:`
          }
        ],
        commands: [
          { cmd: "docker compose -f docker-compose.dev.yml up --build", desc: "Compiles all local Dockerfiles and boots the entire live-reloading e-commerce stack." },
          { cmd: "docker exec -it shop-db psql -U admin -d catalog -c 'SELECT * FROM products;'", desc: "Directly queries the seeded database table records inside the running database container." },
          { cmd: "docker compose logs -f api-server", desc: "Streams logs dynamically from the active Express application to troubleshoot connections." }
        ],
        caseStudy: "<strong>Securing Hot Reloading in Containers:</strong> A common bug when mounting host directories into node containers is the host `node_modules/` overwriting the container's specialized Linux modules. Solve this by declaring an anonymous volume (`/app/node_modules`) in the compose file, which instructs the volume engine to preserve the internal container folder separate from host bindings."
      },
      {
        id: 6,
        title: "Kubernetes Orchestration & Cluster Architecture",
        category: "k8s",
        level: "Fundamentals",
        difficulty: "Intermediate",
        tldr: "Kubernetes is a declarative container coordinator. The Control Plane acts as the brains (State reconciler) while Worker nodes execute container workloads under Kubelet control.",
        def: "When moving to multi-server topologies, single-host Docker is insufficient. <strong>Kubernetes (K8s)</strong> orchestrates hundreds of physical or virtual servers. By comparing actual runtime stats with your desired cluster configurations stored in the <code>etcd</code> datastore, K8s continuously reconciles system states using controller loops.",
        diagram: `
+-------------------------------------------------------------------------------+
|                                 CONTROL PLANE                                 |
|                                                                               |
|  +--------------+       REST      +----------------+       Sync      +-----+  |
|  |  Kube-Admin  |---------------->| Kube-APIServer |---------------->|etcd |  |
|  +--------------+                 +----------------+                 +-----+  |
|                                      ^          ^                             |
|                                      |          |                             |
|                                      v          v                             |
|                           +-------------+   +-----------------------+         |
|                           |  Scheduler  |   |   Controller Manager  |         |
|                           +-------------+   +-----------------------+         |
+--------------------------------------|----------------------------------------+
                                       |
                    Deploy instructions | (gRPC over secure mutual TLS)
                                       v
+-------------------------------------------------------------------------------+
|                                  WORKER NODE                                  |
|                                                                               |
|      +-----------------------------------------+   +--------------------+     |
|      | Kubelet (Node Agent)                    |-->| Kube-Proxy         |     |
|      | - Listens to API Server                 |   | (IPVS / IPTables)  |     |
|      | - Instructs Container Runtime Interface |   +--------------------+     |
|      +-----------------------------------------+                              |
|                          |                                                    |
|                          v                                                    |
|      +-----------------------------------------+                              |
|      | Container Runtime (containerd / Docker) |                              |
|      | - Spawns Pods & Running Containers      |                              |
|      +-----------------------------------------+                              |
+-------------------------------------------------------------------------------+
        `,
        cards: [
          {
            title: "etcd Datastore",
            desc: "Highly-available, distributed key-value database. The single source of truth for the entire cluster's state. All cluster configurations and live object states reside here."
          },
          {
            title: "Kube-APIServer",
            desc: "The gatekeeper for the control plane. Exposes JSON over HTTP APIs. Authenticates requests, validates incoming resource configurations, and is the ONLY component allowed to speak directly to etcd."
          },
          {
            title: "Kubelet Node Loop",
            desc: "An agent executing on every worker node. It registers the node, watches the APIServer for assigned Pod configs, talks to the Container Runtime to deploy containers, and monitors local health states."
          }
        ],
        tabs: [
          {
            name: "cluster-architecture.md",
            code: `<span class="c-comment"># CONTROL PLANE KEY COMPONENT ANALYSIS</span>
- <strong>kube-apiserver:</strong> Scale-out entry point. Scales horizontally. Validates configurations.
- <strong>etcd:</strong> Distributed Raft consensus key-value database. Keeps records of state.
- <strong>kube-scheduler:</strong> Selects appropriate nodes for newly spawned pods. Considers resource bounds, taints/tolerations, affinity, and localized port limits.
- <strong>kube-controller-manager:</strong> Coordinates background loops: Node Controller, Replica Controller, Endpoint Controller, Namespace Controller.

<span class="c-comment"># WORKER NODE SERVICES</span>
- <strong>kubelet:</strong> Acts as physical local node manager. Instructs CRI socket endpoints.
- <strong>kube-proxy:</strong> Handles local node system network port redirects and L4 routing mappings.
- <strong>containerd:</strong> Compiles namespaces, layers, and boots active container software.`
          },
          {
            name: "kubeconfig.yaml",
            code: `<span class="c-k8s-key">apiVersion</span>: <span class="c-string">v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">Config</span>
<span class="c-k8s-key">clusters</span>:
- <span class="c-k8s-key">name</span>: <span class="c-string">prod-cluster</span>
  <span class="c-k8s-key">cluster</span>:
    <span class="c-k8s-key">certificate-authority-data</span>: <span class="c-string">LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t...</span>
    <span class="c-k8s-key">server</span>: <span class="c-string">https://104.20.15.5:6443</span>
<span class="c-k8s-key">contexts</span>:
- <span class="c-k8s-key">name</span>: <span class="c-string">prod-admin-context</span>
  <span class="c-k8s-key">context</span>:
    <span class="c-k8s-key">cluster</span>: <span class="c-string">prod-cluster</span>
    <span class="c-k8s-key">user</span>: <span class="c-string">prod-admin</span>
    <span class="c-k8s-key">namespace</span>: <span class="c-string">production</span>
<span class="c-k8s-key">current-context</span>: <span class="c-string">prod-admin-context</span>
<span class="c-k8s-key">users</span>:
- <span class="c-k8s-key">name</span>: <span class="c-string">prod-admin</span>
  <span class="c-k8s-key">user</span>:
    <span class="c-k8s-key">client-certificate-data</span>: <span class="c-string">LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t...</span>
    <span class="c-k8s-key">client-key-data</span>: <span class="c-string">LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0t...</span>`
          },
          {
            name: "inspect-control-plane.sh",
            code: `<span class="c-comment"># 1. View active system components in kube-system namespace</span>
kubectl get pods -n kube-system

<span class="c-comment"># 2. Extract logs from the API server container</span>
kubectl logs -n kube-system kube-apiserver-master-node-01 --tail=100

<span class="c-comment"># 3. Retrieve system resources support specs and descriptions</span>
kubectl api-resources`
          }
        ],
        commands: [
          { cmd: "kubectl get nodes -o wide", desc: "Retrieves list of registered nodes, showing roles, Kubernetes version, external IPs, OS images, and kernel versions." },
          { cmd: "kubectl get pods -A", desc: "Lists all active pods across every namespace, revealing control plane items running inside kube-system." },
          { cmd: "kubectl describe node master-node-01", desc: "Details resources allocated, limits, capacity, systemic conditions, and events occurring on a specific worker node." }
        ],
        caseStudy: "<strong>Self-Healing Loop in Action:</strong> When you execute `kubectl apply -f deployment.yaml` requesting `replicas: 3`, etcd registers the target configurations. If a physical node fails, taking down Pod 3, the Controller Manager detects that Actual (2 Pods) != Desired (3 Pods). It immediately commands the Scheduler to spin up a new Pod on a healthy node, completing self-healing."
      },
      {
        id: 7,
        title: "Kubernetes Networking & Service Discovery",
        category: "k8s",
        level: "Intermediate",
        difficulty: "Advanced",
        tldr: "K8s networking implements a flat IP model where every Pod has a unique IP. Services expose dynamic pods under stable DNS names, and Ingress routes external traffic.",
        def: "Pod life cycles are ephemeral; IPs change constantly upon node failures. <strong>Services</strong> act as static layer-4 load-balancers that route requests to target Pods matching a label selector. <strong>Ingress</strong> sits at layer-7, routing external HTTP headers and paths to appropriate Services, securing traffic with SSL certificates.",
        diagram: `
                              [ HTTP Request ]
                                     |
                                     v
                        +--------------------------+
                        |  Ingress Controller (L7) |  Hosts: myapp.com/api
                        +--------------------------+
                                     |
                                     v
                        +--------------------------+
                        |   Service: API-Svc (L4)  |  Stable IP: 10.96.4.15
                        +--------------------------+
                                     |
                +--------------------+--------------------+
                | (Load Balances across dynamic Pod IPs)  |
                v                                         v
   +-------------------------+               +-------------------------+
   |      Pod 1 (10.244.1.5) |               |      Pod 2 (10.244.2.8) |
   +-------------------------+               +-------------------------+
        `,
        cards: [
          {
            title: "ClusterIP vs NodePort",
            desc: "ClusterIP (Default) exposes the service on an internal-only IP, secure from public access. NodePort binds a static high-number port (30000-32767) on all physical node interfaces to expose pods."
          },
          {
            title: "Ingress & Path Routing",
            desc: "A declarative Layer-7 proxy controller (typically Nginx Ingress). Evaluates request URLs and HTTP paths, forwarding traffic to corresponding internal services, while terminating TLS certs."
          },
          {
            title: "Network Policies",
            desc: "A cluster firewall mechanism. By default, Pods accept traffic from anywhere. NetworkPolicies restrict traffic flow using label selectors (e.g. only Frontend pods can ping the Database ports)."
          }
        ],
        tabs: [
          {
            name: "service.yaml",
            code: `<span class="c-k8s-key">apiVersion</span>: <span class="c-string">v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">Service</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">api-service</span>
  <span class="c-k8s-key">namespace</span>: <span class="c-string">production</span>
<span class="c-k8s-key">spec</span>:
  <span class="c-k8s-key">type</span>: <span class="c-string">ClusterIP</span> <span class="c-comment"># Accessible strictly inside the cluster</span>
  <span class="c-k8s-key">selector</span>:
    <span class="c-k8s-key">app</span>: <span class="c-string">backend-api</span> <span class="c-comment"># Automatically maps all dynamic Pods carrying this label</span>
  <span class="c-k8s-key">ports</span>:
    - <span class="c-k8s-key">protocol</span>: <span class="c-string">TCP</span>
      <span class="c-k8s-key">port</span>: <span class="c-number">80</span> <span class="c-comment"># Port exposed by the Service IP</span>
      <span class="c-k8s-key">targetPort</span>: <span class="c-number">3000</span> <span class="c-comment"># Port the application listens to in the container</span>`
          },
          {
            name: "ingress.yaml",
            code: `<span class="c-k8s-key">apiVersion</span>: <span class="c-string">networking.k8s.io/v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">Ingress</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">api-ingress</span>
  <span class="c-k8s-key">namespace</span>: <span class="c-string">production</span>
  <span class="c-k8s-key">annotations</span>:
    <span class="c-k8s-key">nginx.ingress.kubernetes.io/ssl-redirect</span>: <span class="c-string">"true"</span>
    <span class="c-k8s-key">nginx.ingress.kubernetes.io/rewrite-target</span>: <span class="c-string">/</span>
<span class="c-k8s-key">spec</span>:
  <span class="c-k8s-key">ingressClassName</span>: <span class="c-string">nginx</span>
  <span class="c-k8s-key">tls</span>:
  - <span class="c-k8s-key">hosts</span>:
    - <span class="c-string">api.myproductiondomain.com</span>
    <span class="c-k8s-key">secretName</span>: <span class="c-string">production-tls-certs</span> <span class="c-comment"># Points to Secret holding SSL keys</span>
  <span class="c-k8s-key">rules</span>:
  - <span class="c-k8s-key">host</span>: <span class="c-string">api.myproductiondomain.com</span>
    <span class="c-k8s-key">http</span>:
      <span class="c-k8s-key">paths</span>:
      - <span class="c-k8s-key">path</span>: <span class="c-string">/</span>
        <span class="c-k8s-key">pathType</span>: <span class="c-string">Prefix</span>
        <span class="c-k8s-key">backend</span>:
          <span class="c-k8s-key">service</span>:
            <span class="c-k8s-key">name</span>: <span class="c-string">api-service</span>
            <span class="c-k8s-key">port</span>:
              <span class="c-k8s-key">number</span>: <span class="c-number">80</span>`
          },
          {
            name: "network-policy.yaml",
            code: `<span class="c-comment"># Strict isolations: Block direct network connections to DB pods</span>
<span class="c-k8s-key">apiVersion</span>: <span class="c-string">networking.k8s.io/v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">NetworkPolicy</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">db-ingress-policy</span>
  <span class="c-k8s-key">namespace</span>: <span class="c-string">production</span>
<span class="c-k8s-key">spec</span>:
  <span class="c-k8s-key">podSelector</span>:
    <span class="c-k8s-key">matchLabels</span>:
      <span class="c-k8s-key">app</span>: <span class="c-string">postgres-db</span> <span class="c-comment"># Apply policy strictly to Postgres pods</span>
  <span class="c-k8s-key">policyTypes</span>:
  - <span class="c-k8s-key">Ingress</span>
  <span class="c-k8s-key">ingress</span>:
  - <span class="c-k8s-key">from</span>:
    - <span class="c-k8s-key">podSelector</span>:
        <span class="c-k8s-key">matchLabels</span>:
          <span class="c-k8s-key">app</span>: <span class="c-string">backend-api</span> <span class="c-comment"># Permitted ingress source</span>
    <span class="c-k8s-key">ports</span>:
    - <span class="c-k8s-key">protocol</span>: <span class="c-string">TCP</span>
      <span class="c-k8s-key">port</span>: <span class="c-number">5432</span>`
          }
        ],
        commands: [
          { cmd: "kubectl get svc -n production", desc: "Lists all exposed services, revealing internal ClusterIPs, NodePorts, and active external LoadBalancer IPs." },
          { cmd: "kubectl describe ingress api-ingress -n production", desc: "Prints rule configurations, host maps, TLS settings, path resolutions, and target backends." },
          { cmd: "kubectl exec -it production-api-5c798dff7f-8x2kl -- nslookup api-service", desc: "Executes an interactive shell DNS lookup check inside a running pod to audit CoreDNS service discovery resolution." }
        ],
        caseStudy: "<strong>Dynamic Endpoints Resolution:</strong> When Pods scale or crash, their dynamic IPs are removed from the system. Kube-proxy monitors these changes and dynamically rewrites IPVS/IPTables rules on all nodes to direct Service IP traffic directly to the remaining healthy target Pod endpoints."
      },
      {
        id: 8,
        title: "Kubernetes Storage & Persistent Volumes",
        category: "k8s",
        level: "Intermediate",
        difficulty: "Intermediate",
        tldr: "Pods are ephemeral; local container filesystem changes are lost upon crash or deletion. Decouple storage using PersistentVolumes, claims, and StorageClasses.",
        def: "Stateful systems like databases require durable disk architectures. Kubernetes separates infrastructure storage allocations from developer consumption. Admins or cloud engines declare <strong>PersistentVolumes (PV)</strong>, developers make <strong>PersistentVolumeClaims (PVC)</strong> to request capacity, and <strong>StorageClasses</strong> dynamically orchestrate provisioning of network-attached cloud blocks.",
        diagram: `
   +-------------------------+
   |      Application Pod    |  <- References PVC to mount directory
   +-------------------------+
                |
                v  Mounts Volume
   +-------------------------+
   |  PersistentVolumeClaim  |  <- Developer-facing storage request
   |  (Request: 20Gi Read)   |
   +-------------------------+
                |
                v  Binds dynamically
   +-------------------------+
   |    PersistentVolume     |  <- cluster-level storage resource
   |    (Allocated: 20Gi)    |
   +-------------------------+
                |
                v  API Provisions Block
   +-------------------------+
   | Cloud Disk (AWS gp3 /   |  <- Physical network-attached storage
   | Azure Disk / Local Disk)|
   +-------------------------+
        `,
        cards: [
          {
            title: "PV vs PVC Separation",
            desc: "PersistentVolume (PV) represents the raw physical storage resource. PersistentVolumeClaim (PVC) acts as a voucher used by developers to request specific sizing and access modes (ReadWriteOnce vs ReadWriteMany)."
          },
          {
            title: "Dynamic Storage Classes",
            desc: "Eliminates pre-provisioning. When a developer submits a PVC referencing a StorageClass, the cloud driver automatically provisions the underlying block storage and binds it to a created PV."
          },
          {
            title: "ConfigMaps & Secrets",
            desc: "Mount static configurations (JSON/YAML) or base64 encoded sensitive keys directly as environmental keys or dynamic files in container paths, without rebuilding images."
          }
        ],
        tabs: [
          {
            name: "storage-class.yaml",
            code: `<span class="c-k8s-key">apiVersion</span>: <span class="c-string">storage.k8s.io/v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">StorageClass</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">production-ssd</span>
<span class="c-k8s-key">provisioner</span>: <span class="c-string">ebs.csi.aws.com</span> <span class="c-comment"># AWS CSI Driver</span>
<span class="c-k8s-key">volumeBindingMode</span>: <span class="c-string">WaitForFirstConsumer</span> <span class="c-comment"># Delay allocation until Pod scheduling knows the target node's Availability Zone</span>
<span class="c-k8s-key">parameters</span>:
  <span class="c-k8s-key">type</span>: <span class="c-string">gp3</span>
  <span class="c-k8s-key">iops</span>: <span class="c-string">"3000"</span>`
          },
          {
            name: "postgres-stateful-storage.yaml",
            code: `<span class="c-k8s-key">apiVersion</span>: <span class="c-string">v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">PersistentVolumeClaim</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">postgres-pvc</span>
  <span class="c-k8s-key">namespace</span>: <span class="c-string">production</span>
<span class="c-k8s-key">spec</span>:
  <span class="c-k8s-key">accessModes</span>:
    - <span class="c-string">ReadWriteOnce</span> <span class="c-comment"># Only mountable by a single node at a time</span>
  <span class="c-k8s-key">storageClassName</span>: <span class="c-string">production-ssd</span>
  <span class="c-k8s-key">resources</span>:
    <span class="c-k8s-key">requests</span>:
      <span class="c-k8s-key">storage</span>: <span class="c-string">20Gi</span>`
          },
          {
            name: "configmap-secrets.yaml",
            code: `<span class="c-k8s-key">apiVersion</span>: <span class="c-string">v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">Secret</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">database-secret</span>
  <span class="c-k8s-key">namespace</span>: <span class="c-string">production</span>
<span class="c-k8s-key">type</span>: <span class="c-string">Opaque</span>
<span class="c-k8s-key">data</span>:
  <span class="c-comment"># db-password base64 encoded: secureVault991</span>
  <span class="c-k8s-key">db-password</span>: <span class="c-string">c2VjdXJlVmF1bHQ5OTE=</span>
---
<span class="c-k8s-key">apiVersion</span>: <span class="c-string">v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">ConfigMap</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">api-config</span>
  <span class="c-k8s-key">namespace</span>: <span class="c-string">production</span>
<span class="c-k8s-key">data</span>:
  <span class="c-k8s-key">LOG_LEVEL</span>: <span class="c-string">"info"</span>
  <span class="c-k8s-key">CACHE_TTL</span>: <span class="c-string">"3600"</span>`
          }
        ],
        commands: [
          { cmd: "kubectl get pv", desc: "Queries all persistent volumes defined across the cluster, highlighting capacities, access patterns, and binds." },
          { cmd: "kubectl get pvc -n production", desc: "Lists claims requested, reporting dynamic statuses (BOUND, PENDING, or LOST)." },
          { cmd: "kubectl describe secret database-secret -n production", desc: "Retrieves metadata regarding sensitive secrets, keeping key values hidden until explicitly unpacked." }
        ],
        caseStudy: "<strong>Dynamic AZ Scheduling:</strong> Setting `volumeBindingMode: WaitForFirstConsumer` is critical. If storage is provisioned immediately in Zone A, but resources require the target Pod to launch in Zone B, the Pod becomes unschedulable. Delaying provisioning guarantees the cloud disk aligns with the node selected by the Scheduler."
      },
      {
        id: 9,
        title: "Advanced Scheduling, Lifecycle & Probes",
        category: "k8s",
        level: "Advanced",
        difficulty: "Advanced",
        tldr: "Deploying updates requires safety guarantees. Master StatefulSets, DaemonSets, CronJobs, and critical Startup, Liveness, and Readiness health probes.",
        def: "Kubernetes coordinates rolling updates automatically, but your application must communicate its runtime readiness. By configuring <strong>Readiness Probes</strong> to prevent traffic routing to warm-up nodes, and <strong>Liveness Probes</strong> to restart deadlocked processes, you execute zero-downtime deployments with ultimate security.",
        diagram: `
                  [ HTTP Probe request to endpoint /healthz ]
                                     |
                                     v
                 +---------------------------------------+
                 |  STARTUP PROBE: Check if booting up   |
                 +---------------------------------------+
                    |                               |
           Success  |                       Fail    |  Restarts container
                    v                               v  after threshold
                 +---------------------------------------+
                 |  LIVENESS PROBE: Is app deadlocked?   |
                 +---------------------------------------+
                    |                               |
           Success  |                       Fail    |  Restarts container
                    v                               v  for self-healing
                 +---------------------------------------+
                 |  READINESS PROBE: Can app take load?  |
                 +---------------------------------------+
                    |                               |
           Success  |                       Fail    |  Removes Pod from
                    v                               v  Service endpoint list
         [ Route Active Traffic ]                [ Temporarily isolate ]
        `,
        cards: [
          {
            title: "Readiness vs Liveness",
            desc: "Liveness probes trigger restarts for deadlocked/stuck containers. Readiness probes temporarily isolate containers from service discovery pools if they're busy executing warm-ups or intensive migrations."
          },
          {
            title: "StatefulSets & Stable Identity",
            desc: "For databases. Unlike regular Deployments, StatefulSet Pods are assigned ordinal index IDs (db-0, db-1) and stable network hostnames, binding permanently to their respective persistent volumes."
          },
          {
            title: "DaemonSets & Node Agents",
            desc: "Deploys exactly one copy of a Pod to every single worker node in the cluster. Standard design for background monitoring, metric shipping (Prometheus), or file log collection (Fluentd)."
          }
        ],
        tabs: [
          {
            name: "deployment-probes.yaml",
            code: `<span class="c-k8s-key">apiVersion</span>: <span class="c-string">apps/v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">Deployment</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">robust-api</span>
  <span class="c-k8s-key">namespace</span>: <span class="c-string">production</span>
<span class="c-k8s-key">spec</span>:
  <span class="c-k8s-key">replicas</span>: <span class="c-number">3</span>
  <span class="c-k8s-key">strategy</span>:
    <span class="c-k8s-key">type</span>: <span class="c-string">RollingUpdate</span>
    <span class="c-k8s-key">rollingUpdate</span>:
      <span class="c-k8s-key">maxSurge</span>: <span class="c-string">25%</span>
      <span class="c-k8s-key">maxUnavailable</span>: <span class="c-string">0</span>
  <span class="c-k8s-key">selector</span>:
    <span class="c-k8s-key">matchLabels</span>:
      <span class="c-k8s-key">app</span>: <span class="c-string">robust-api</span>
  <span class="c-k8s-key">template</span>:
    <span class="c-k8s-key">metadata</span>:
      <span class="c-k8s-key">labels</span>:
        <span class="c-k8s-key">app</span>: <span class="c-string">robust-api</span>
    <span class="c-k8s-key">spec</span>:
      <span class="c-k8s-key">containers</span>:
      - <span class="c-k8s-key">name</span>: <span class="c-string">api-container</span>
        <span class="c-k8s-key">image</span>: <span class="c-string">myregistry.com/app:2.1.0</span>
        <span class="c-k8s-key">ports</span>:
        - <span class="c-k8s-key">containerPort</span>: <span class="c-number">3000</span>
        
        <span class="c-k8s-key">startupProbe</span>:
          <span class="c-k8s-key">httpGet</span>:
            <span class="c-k8s-key">path</span>: <span class="c-string">/healthz/startup</span>
            <span class="c-k8s-key">port</span>: <span class="c-number">3000</span>
          <span class="c-k8s-key">failureThreshold</span>: <span class="c-number">30</span>
          <span class="c-k8s-key">periodSeconds</span>: <span class="c-number">10</span>

        <span class="c-k8s-key">livenessProbe</span>:
          <span class="c-k8s-key">httpGet</span>:
            <span class="c-k8s-key">path</span>: <span class="c-string">/healthz/liveness</span>
            <span class="c-k8s-key">port</span>: <span class="c-number">3000</span>
          <span class="c-k8s-key">periodSeconds</span>: <span class="c-number">15</span>
          <span class="c-k8s-key">timeoutSeconds</span>: <span class="c-number">5</span>
          <span class="c-k8s-key">failureThreshold</span>: <span class="c-number">3</span>

        <span class="c-k8s-key">readinessProbe</span>:
          <span class="c-k8s-key">httpGet</span>:
            <span class="c-k8s-key">path</span>: <span class="c-string">/healthz/readiness</span>
            <span class="c-k8s-key">port</span>: <span class="c-number">3000</span>
          <span class="c-k8s-key">periodSeconds</span>: <span class="c-number">10</span>
          <span class="c-k8s-key">successThreshold</span>: <span class="c-number">1</span>
          <span class="c-k8s-key">failureThreshold</span>: <span class="c-number">2</span>`
          },
          {
            name: "statefulset-db.yaml",
            code: `<span class="c-k8s-key">apiVersion</span>: <span class="c-string">apps/v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">StatefulSet</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">cluster-db</span>
  <span class="c-k8s-key">namespace</span>: <span class="c-string">production</span>
<span class="c-k8s-key">spec</span>:
  <span class="c-k8s-key">serviceName</span>: <span class="c-string">"postgres-hsvc"</span> <span class="c-comment"># Headless service for network identity</span>
  <span class="c-k8s-key">replicas</span>: <span class="c-number">2</span>
  <span class="c-k8s-key">selector</span>:
    <span class="c-k8s-key">matchLabels</span>:
      <span class="c-k8s-key">app</span>: <span class="c-string">postgres-cluster</span>
  <span class="c-k8s-key">template</span>:
    <span class="c-k8s-key">metadata</span>:
      <span class="c-k8s-key">labels</span>:
        <span class="c-k8s-key">app</span>: <span class="c-string">postgres-cluster</span>
    <span class="c-k8s-key">spec</span>:
      <span class="c-k8s-key">containers</span>:
      - <span class="c-k8s-key">name</span>: <span class="c-string">postgres</span>
        <span class="c-k8s-key">image</span>: <span class="c-string">postgres:15-alpine</span>
        <span class="c-k8s-key">volumeMounts</span>:
        - <span class="c-k8s-key">name</span>: <span class="c-string">db-vol</span>
          <span class="c-k8s-key">mountPath</span>: <span class="c-string">/var/lib/postgresql/data</span>
  <span class="c-k8s-key">volumeClaimTemplates</span>: <span class="c-comment"># Automatically creates PVC per replica</span>
  - <span class="c-k8s-key">metadata</span>:
      <span class="c-k8s-key">name</span>: <span class="c-string">db-vol</span>
    <span class="c-k8s-key">spec</span>:
      <span class="c-k8s-key">accessModes</span>: [ <span class="c-string">"ReadWriteOnce"</span> ]
      <span class="c-k8s-key">resources</span>:
        <span class="c-k8s-key">requests</span>:
          <span class="c-k8s-key">storage</span>: <span class="c-string">10Gi</span>`
          },
          {
            name: "cronjob-backup.yaml",
            code: `<span class="c-k8s-key">apiVersion</span>: <span class="c-string">batch/v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">CronJob</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">database-backup</span>
  <span class="c-k8s-key">namespace</span>: <span class="c-string">production</span>
<span class="c-k8s-key">spec</span>:
  <span class="c-k8s-key">schedule</span>: <span class="c-string">"0 2 * * *"</span> <span class="c-comment"># Daily at 2 AM</span>
  <span class="c-k8s-key">jobTemplate</span>:
    <span class="c-k8s-key">spec</span>:
      <span class="c-k8s-key">template</span>:
        <span class="c-k8s-key">spec</span>:
          <span class="c-k8s-key">containers</span>:
          - <span class="c-k8s-key">name</span>: <span class="c-string">backup-tool</span>
            <span class="c-k8s-key">image</span>: <span class="c-string">myregistry.com/backup-utility:latest</span>
          <span class="c-k8s-key">restartPolicy</span>: <span class="c-string">OnFailure</span>`
          }
        ],
        commands: [
          { cmd: "kubectl rollout status deployment/robust-api -n production", desc: "Monitors progress of rolling upgrades, exiting cleanly once state resolves successfully." },
          { cmd: "kubectl rollout undo deployment/robust-api -n production", desc: "Rolls back to the previous deployment revision instantly, performing zero-downtime self-recovery." },
          { cmd: "kubectl get events -w -n production", desc: "Streams cluster-level events, revealing scheduling failures, health check violations, or node restarts." }
        ],
        caseStudy: "<strong>Avoid Cascade Restart Disasters:</strong> Without `startupProbe`, setting `initialDelaySeconds` too low on a liveness probe causes a major bug: K8s ping-pongs the container before it finishes compiling assets, crashing it repeatedly in an endless startup reboot loop."
      },
      {
        id: 10,
        title: "Enterprise Production Project - Banking Ledger System",
        category: "k8s",
        level: "Advanced",
        difficulty: "Expert",
        tldr: "Synthesize all principles. Build a highly available, securely hardened, autoscaled financial transaction ledger stack ready for production-grade traffic.",
        def: "Deploying a single isolated container is simple. Deploying a production application requires orchestrating dynamic horizontal autoscaling (HPA), enforcing strict kernel access rules (SecurityContext), reserving exact hardware slices (requests & limits), and managing configuration templates cleanly across secure environments.",
        diagram: `
                                     [ INGRESS (https://mybank.com) ]
                                                    |
                                                    v
                                    +------------------------------+
                                    |     api-service (Service)    |
                                    +------------------------------+
                                                    |
                                                    v
                                 +------------------------------------+
                                 |  api-deployment (Pods - Autoscaled)|
                                 |  HPA Limits: Min 2 - Max 10 Pods   |
                                 +------------------------------------+
                                         |                    |
                                         | tcp://             | tcp://
                                         v                    v
                        +--------------------+            +--------------------+
                        | redis-svc (Cache)  |            | postgres-svc (DB)  |
                        +--------------------+            +--------------------+
        `,
        cards: [
          {
            title: "Resource Slicing (Limits)",
            desc: "Declare strict 'requests' (minimum dedicated scheduler guarantees) and 'limits' (maximum ceiling cut-offs) to prevent noisy neighbor scenarios from starving memory pools."
          },
          {
            title: "Horizontal Pod Autoscaler (HPA)",
            desc: "Binds to cluster metrics API. Periodically polls pods for CPU/Memory utilization, dynamically scaling replicas count up to 10 instances during traffic spikes and scaling back to save costs."
          },
          {
            title: "Security Context Hardening",
            desc: "Disallows running processes as root, disables privilege escalations, restricts write actions to standard runtime volumes, and locks underlying host system calls."
          }
        ],
        tabs: [
          {
            name: "banking-ledger.yaml",
            code: `<span class="c-k8s-key">apiVersion</span>: <span class="c-string">apps/v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">Deployment</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">production-api</span>
  <span class="c-k8s-key">namespace</span>: <span class="c-string">banking</span>
  <span class="c-k8s-key">labels</span>:
    <span class="c-k8s-key">tier</span>: <span class="c-string">backend</span>
<span class="c-k8s-key">spec</span>:
  <span class="c-k8s-key">replicas</span>: <span class="c-number">2</span>
  <span class="c-k8s-key">selector</span>:
    <span class="c-k8s-key">matchLabels</span>:
      <span class="c-k8s-key">app</span>: <span class="c-string">production-api</span>
  <span class="c-k8s-key">template</span>:
    <span class="c-k8s-key">metadata</span>:
      <span class="c-k8s-key">labels</span>:
        <span class="c-k8s-key">app</span>: <span class="c-string">production-api</span>
    <span class="c-k8s-key">spec</span>:
      <span class="c-comment"># Hardened Pod Security</span>
      <span class="c-k8s-key">securityContext</span>:
        <span class="c-k8s-key">runAsNonRoot</span>: <span class="c-string">true</span>
        <span class="c-k8s-key">runAsUser</span>: <span class="c-number">10001</span>
        <span class="c-k8s-key">fsGroup</span>: <span class="c-number">20001</span>
      
      <span class="c-k8s-key">containers</span>:
      - <span class="c-k8s-key">name</span>: <span class="c-string">api-runner</span>
        <span class="c-k8s-key">image</span>: <span class="c-string">myregistry.com/banking-api:v1.2.0</span>
        
        <span class="c-comment"># Enforced Sandbox restrictions</span>
        <span class="c-k8s-key">securityContext</span>:
          <span class="c-k8s-key">allowPrivilegeEscalation</span>: <span class="c-string">false</span>
          <span class="c-k8s-key">readOnlyRootFilesystem</span>: <span class="c-string">true</span> <span class="c-comment"># Block file modification exploits</span>
          <span class="c-k8s-key">capabilities</span>:
            <span class="c-k8s-key">drop</span>:
            - <span class="c-string">ALL</span>
            
        <span class="c-comment"># Resource Requests & Limits</span>
        <span class="c-k8s-key">resources</span>:
          <span class="c-k8s-key">requests</span>:
            <span class="c-k8s-key">memory</span>: <span class="c-string">"256Mi"</span>
            <span class="c-k8s-key">cpu</span>: <span class="c-string">"100m"</span>
          <span class="c-k8s-key">limits</span>:
            <span class="c-k8s-key">memory</span>: <span class="c-string">"512Mi"</span>
            <span class="c-k8s-key">cpu</span>: <span class="c-string">"500m"</span>
            
        <span class="c-comment"># Mount temporary files for runtime writes</span>
        <span class="c-k8s-key">volumeMounts</span>:
        - <span class="c-k8s-key">name</span>: <span class="c-string">tmp-volume</span>
          <span class="c-k8s-key">mountPath</span>: <span class="c-string">/tmp</span>
          
        <span class="c-k8s-key">env</span>:
        - <span class="c-k8s-key">name</span>: <span class="c-string">DB_PASSWORD</span>
          <span class="c-k8s-key">valueFrom</span>:
            <span class="c-k8s-key">secretKeyRef</span>:
              <span class="c-k8s-key">name</span>: <span class="c-string">database-secret</span>
              <span class="c-k8s-key">key</span>: <span class="c-string">db-password</span>
              
      <span class="c-k8s-key">volumes</span>:
      - <span class="c-k8s-key">name</span>: <span class="c-string">tmp-volume</span>
        <span class="c-k8s-key">emptyDir</span>: {}`
          },
          {
            name: "database-statefulset.yaml",
            code: `<span class="c-k8s-key">apiVersion</span>: <span class="c-string">apps/v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">StatefulSet</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">ledger-db</span>
  <span class="c-k8s-key">namespace</span>: <span class="c-string">banking</span>
<span class="c-k8s-key">spec</span>:
  <span class="c-k8s-key">serviceName</span>: <span class="c-string">"db-headless"</span>
  <span class="c-k8s-key">replicas</span>: <span class="c-number">3</span>
  <span class="c-k8s-key">template</span>:
    <span class="c-k8s-key">spec</span>:
      <span class="c-k8s-key">containers</span>:
      - <span class="c-k8s-key">name</span>: <span class="c-string">postgres</span>
        <span class="c-k8s-key">image</span>: <span class="c-string">postgres:15-alpine</span>
        <span class="c-k8s-key">volumeMounts</span>:
        - <span class="c-k8s-key">name</span>: <span class="c-string">db-data</span>
          <span class="c-k8s-key">mountPath</span>: <span class="c-string">/var/lib/postgresql/data</span>
  <span class="c-k8s-key">volumeClaimTemplates</span>:
  - <span class="c-k8s-key">metadata</span>:
      <span class="c-k8s-key">name</span>: <span class="c-string">db-data</span>
    <span class="c-k8s-key">spec</span>:
      <span class="c-k8s-key">accessModes</span>: [ <span class="c-string">"ReadWriteOnce"</span> ]
      <span class="c-k8s-key">storageClassName</span>: <span class="c-string">production-ssd</span>
      <span class="c-k8s-key">resources</span>:
        <span class="c-k8s-key">requests</span>:
          <span class="c-k8s-key">storage</span>: <span class="c-string">50Gi</span>`
          },
          {
            name: "ingress-tls.yaml",
            code: `<span class="c-k8s-key">apiVersion</span>: <span class="c-string">networking.k8s.io/v1</span>
<span class="c-k8s-key">kind</span>: <span class="c-string">Ingress</span>
<span class="c-k8s-key">metadata</span>:
  <span class="c-k8s-key">name</span>: <span class="c-string">banking-ingress</span>
  <span class="c-k8s-key">namespace</span>: <span class="c-string">banking</span>
  <span class="c-k8s-key">annotations</span>:
    <span class="c-k8s-key">cert-manager.io/cluster-issuer</span>: <span class="c-string">"letsencrypt-prod"</span>
<span class="c-k8s-key">spec</span>:
  <span class="c-k8s-key">ingressClassName</span>: <span class="c-string">nginx</span>
  <span class="c-k8s-key">tls</span>:
  - <span class="c-k8s-key">hosts</span>:
    - <span class="c-string">ledger.mybank.com</span>
    <span class="c-k8s-key">secretName</span>: <span class="c-string">ledger-tls-certs</span>
  <span class="c-k8s-key">rules</span>:
  - <span class="c-k8s-key">host</span>: <span class="c-string">ledger.mybank.com</span>
    <span class="c-k8s-key">http</span>:
      <span class="c-k8s-key">paths</span>:
      - <span class="c-k8s-key">path</span>: <span class="c-string">/</span>
        <span class="c-k8s-key">pathType</span>: <span class="c-string">Prefix</span>
        <span class="c-k8s-key">backend</span>:
          <span class="c-k8s-key">service</span>:
            <span class="c-k8s-key">name</span>: <span class="c-string">production-api-svc</span>
            <span class="c-k8s-key">port</span>:
              <span class="c-k8s-key">number</span>: <span class="c-number">80</span>`
          }
        ],
        commands: [
          { cmd: "kubectl apply -f banking-ledger.yaml", desc: "Deploys the entire production resources set into the cluster namespace." },
          { cmd: "kubectl get pods -n banking", desc: "Monitors dynamic scale actions, detailing targets, thresholds, and live capacities." },
          { cmd: "kubectl get hpa -n banking", desc: "Displays current CPU and memory utilization metrics of running pods in real-time." }
        ],
        caseStudy: "<strong>ReadOnlyRootFilesystem Strategy:</strong> Marking the root directory as read-only is the most effective way to secure a container. In the manifest above, if an attacker executes code injection, they cannot write malicious binaries to `/bin` or `/usr`. They can only write to the temporary `/tmp` mount, which is backed by a transient memory-based `emptyDir` volume."
      }
    ];"""

new_terminal_js = """// ── MOCK TERMINAL SIMULATOR DATABASE ──
    const terminalCommands = {
      "docker --version": "Docker version 24.0.7, build afdd53b",
      
      "kubectl cluster-info": `Kubernetes control plane is running at https://127.0.0.1:6443
CoreDNS is running at https://127.0.0.1:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.`,

      "kind create cluster --name dev-cluster": `Creating cluster "dev-cluster" ...
 ✓ Ensuring node image (kindest/node:v1.28.2) 🖼
 ✓ Preparing nodes 📦 📦 📦 
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
 ✓ Joining worker nodes 🔗 
Set kubectl context to "kind-dev-cluster"
You can now use your cluster with: kubectl cluster-info --context kind-dev-cluster`,

      "docker ps": `CONTAINER ID   IMAGE                 COMMAND                  CREATED         STATUS                   PORTS                    NAMES
8b5f9c42ae3a   nginx:alpine          "/docker-entrypoint.…"   2 hours ago     Up 2 hours               0.0.0.0:8080->80/tcp     web-server
2c4d6a1b8e9f   postgres:15-alpine    "docker-entrypoint.s…"   5 hours ago     Up 5 hours (healthy)     5432/tcp                 production-db
a1f2e3d4c5b6   myregistry/api:1.2    "node dist/main.js"      5 mins ago      Up 5 mins                0.0.0.0:5000->3000/tcp   backend-api`,
      
      "docker stats": `CONTAINER ID   NAME            CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O         PIDS
8b5f9c42ae3a   web-server      0.02%     4.15MiB / 15.95GiB    0.03%     1.2kB / 650B      0B / 0B           2
2c4d6a1b8e9f   production-db   0.15%     35.8MiB / 512MiB      6.99%     8.5kB / 12.2kB    45.1kB / 120MB    8
a1f2e3d4c5b6   backend-api     1.85%     128.4MiB / 512MiB     25.08%    15.4kB / 85.2kB   0B / 12.5MB       15`,

      "docker inspect web-server": `[
    {
        "Id": "8b5f9c42ae3ad624f2b963a7d4a2752b57560a671158fdf8fdf8e63b65ef3dfc",
        "Created": "2026-05-18T04:22:15.12356Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [ "nginx", "-g", "daemon off;" ],
        "State": { "Status": "running", "Running": true, "Pid": 12053 },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/c7e2b83efc7d/diff",
                "MergedDir": "/var/lib/docker/overlay2/a1f592cd215e/merged",
                "UpperDir": "/var/lib/docker/overlay2/a1f592cd215e/diff"
            },
            "Name": "overlay2"
        }
    }
]`,

      "lsns -t pid": `        NS TYPE      NPROCS   PID USER COMMAND
4026531836 pid            2 12053 root nginx: master process nginx -g daemon off;
4026531836 pid            2 12089 unit nginx: worker process`,

      "docker build --no-cache -t app:latest .": `Sending build context to Docker daemon  24.52kB
Step 1/14 : FROM node:20-alpine AS builder
 ---> f5e32a67e411
Step 2/14 : WORKDIR /usr/src/app
 ---> Running in a6fdf1cf8743
 ---> Removed intermediate container a6fdf1cf8743
 ---> bd8f8d9f1025
Step 3/14 : COPY package*.json ./
 ---> 5fd2b6ef72e0
Step 4/14 : RUN npm ci
 ---> Running in b5e672a912ef
npm info it worked - ok
added 254 packages in 4.25s
 ---> 3cd8f1ef920c
Successfully built 8cf2e4d6a1b8
Successfully tagged app:latest`,

      "docker history app:latest": `IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
8cf2e4d6a1b8   5 seconds ago    ENTRYPOINT ["node" "dist/main.js"]              0B        
<missing>      5 seconds ago    EXPOSE 3000                                     0B        
<missing>      10 seconds ago   COPY --from=builder /usr/src/app/dist ./dist    1.25MB    
<missing>      12 seconds ago   COPY --from=builder /usr/src/app/node_modules…  48.2MB    
<missing>      2 minutes ago    RUN npm ci                                      52.4MB    `,

      "trivy image app:latest": `Target: app:latest (alpine 3.18.4)
==================================
Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)
No vulnerabilities found!`,

      "docker compose up -d": `[+] Running 3/3
 ⠿ Network db-network      Created                                                          0.1s
 ⠿ Container production-db Healthy                                                          4.5s
 ⠿ Container backend-api   Started                                                          0.8s`,

      "docker compose ps": `NAME            IMAGE                COMMAND                  SERVICE       STATUS        PORTS
backend-api     myregistry/api:1.2   "node dist/main.js"      backend-api   running       0.0.0.0:5000->3000/tcp
production-db   postgres:15-alpine   "docker-entrypoint.s…"   postgres-db   running       5432/tcp`,

      "docker compose -f docker-compose.dev.yml up --build": `[+] Building 0.0s (0/0)
[+] Running 3/3
 ⠿ Network shop-net      Created                                                            0.1s
 ⠿ Container shop-db     Healthy                                                            3.2s
 ⠿ Container api-server  Started                                                            0.5s`,

      "docker exec -it shop-db psql -U admin -d catalog -c 'SELECT * FROM products;'": ` id |       name       |  price   |    category    
----+------------------+----------+----------------
  1 | Wireless Mouse   |    29.99 | Electronics
  2 | Mechanical KB    |    89.99 | Electronics
  3 | USB-C Hub        |    19.99 | Accessories
(3 rows)`,

      "docker compose logs -f api-server": `api-server  | Database connected successfully.
api-server  | Redis connection established.
api-server  | E-Commerce API Server listening on port 5000...`,

      "kubectl get nodes": `NAME             STATUS   ROLES           AGE   VERSION
master-node-01   Ready    control-plane   34d   v1.28.2
worker-node-01   Ready    <none>          34d   v1.28.2
worker-node-02   Ready    <none>          34d   v1.28.2`,

      "kubectl get pods -A": `NAMESPACE     NAME                                     READY   STATUS    RESTARTS   AGE
kube-system   coredns-5d78c9869-7x2kl                  1/1     Running   0          34d
kube-system   etcd-master-node-01                      1/1     Running   0          34d
kube-system   kube-apiserver-master-node-01            1/1     Running   0          34d
kube-system   kube-controller-manager-master-node-01   1/1     Running   0          34d
kube-system   kube-proxy-8x9fd                         1/1     Running   0          34d
production    production-api-5c798dff7f-8x2kl          1/1     Running   0          5m`,

      "kubectl describe node master-node-01": `Name:               master-node-01
Roles:              control-plane
Conditions:
  Type             Status  LastHeartbeatTime                 Reason
  ----             ------  -----------------                 ------
  Ready            True    Mon, 18 May 2026 06:40:12 +0000   KubeletReady
Allocated resources:
  Resource         Requests    Limits
  --------         --------    ------
  cpu              750m (18%)  2000m (50%)
  memory           1.2Gi (15%) 4Gi (50%)`,

      "kubectl get svc -n production": `NAME          TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
api-service   ClusterIP   10.96.4.15    <none>        80/TCP    12m
database-svc  ClusterIP   10.96.12.82   <none>        5432/TCP  18h`,

      "kubectl describe ingress api-ingress -n production": `Name:             api-ingress
Namespace:        production
Address:          192.168.1.100
Ingress Class:    nginx
Rules:
  Host                         Path  Backends
  ----                         ----  --------
  api.myproductiondomain.com   /     api-service:80 (10.244.1.5:3000, 10.244.2.8:3000)
TLS:
  production-tls-certs terminates api.myproductiondomain.com`,

      "kubectl exec -it production-api-5c798dff7f-8x2kl -- nslookup api-service": `Server:         10.96.0.10
Address:        10.96.0.10#53

Name:   api-service.production.svc.cluster.local
Address: 10.96.4.15`,

      "kubectl get pv": `NAME             CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                    STORAGECLASS     AGE
pv-volume-01     20Gi       RWO            Retain           Bound    production/postgres-pvc  production-ssd   18h`,

      "kubectl get pvc -n production": `NAME           STATUS   VOLUME         CAPACITY   ACCESS MODES   STORAGECLASS     AGE
postgres-pvc   Bound    pv-volume-01   20Gi       RWO            production-ssd   18h`,

      "kubectl describe secret database-secret -n production": `Name:         database-secret
Namespace:    production
Type:         Opaque

Data
====
db-password:  14 bytes`,

      "kubectl rollout status deployment/robust-api -n production": "Waiting for deployment \"robust-api\" rollout to finish: 1 of 3 updated replicas are available...\ndeployment \"robust-api\" successfully rolled out",

      "kubectl rollout status deployment/production-api -n production": "Waiting for deployment \"production-api\" rollout to finish: 2 of 2 updated replicas are available...\ndeployment \"production-api\" successfully rolled out",

      "kubectl rollout undo deployment/robust-api -n production": "deployment.apps/robust-api rolled back",

      "kubectl get events -w -n production": `LAST SEEN   TYPE     REASON             OBJECT            MESSAGE
0s          Normal   Scheduled          pod/robust-api-2  Successfully assigned production/robust-api-2 to worker-node-02
1s          Normal   Pulling            pod/robust-api-2  Pulling image "myregistry.com/app:2.1.0"
3s          Normal   Pulled             pod/robust-api-2  Successfully pulled image "myregistry.com/app:2.1.0" in 2.1s
4s          Normal   Created            pod/robust-api-2  Created container api-container
4s          Normal   Started            pod/robust-api-2  Started container api-container`,

      "kubectl apply -f banking-ledger.yaml": `namespace/banking created
secret/database-secret created
configmap/api-config created
deployment.apps/production-api created
service/production-api-svc created
horizontalpodautoscaler.autoscaling/production-api-hpa created
poddisruptionbudget.policy/production-api-pdb created`,

      "kubectl get pods -n banking": `NAME                              READY   STATUS    RESTARTS   AGE
production-api-6b8f9a2d3c-5x8kl   1/1     Running   0          42s
production-api-6b8f9a2d3c-9m4fd   1/1     Running   0          40s`,

      "kubectl get hpa -n banking": `NAME                 REFERENCE                   TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
production-api-hpa   Deployment/production-api   18%/70%   2         10        2          5m`,

      "clear": ""
    };"""

# Compile regex to match the modules array and terminalCommands map in the HTML source code
# We want to replace everything from `// ── DATA DEFINITION ──` up to the end of the `terminalCommands` definition block `};`
# Let's perform a simple, robust string replace or a regex-based replacement.

# Let's locate the starting position of `// ── DATA DEFINITION ──`
start_marker = "// ── DATA DEFINITION ──"
end_marker = "    };"

# Since we want to make sure it's the exact end of terminalCommands, we look for the transition to:
# `// ── JAVASCRIPT APP STATE & NAVIGATION ──`
trans_marker = "// ── JAVASCRIPT APP STATE & NAVIGATION ──"

start_idx = html_content.find(start_marker)
if start_idx == -1:
    print("Error: Could not find start marker!")
    exit(1)

trans_idx = html_content.find(trans_marker)
if trans_idx == -1:
    print("Error: Could not find transition marker!")
    exit(1)

# Now, we search backwards from `trans_idx` to find the closing `};` of terminalCommands
end_idx = html_content.rfind(end_marker, start_idx, trans_idx)
if end_idx == -1:
    print("Error: Could not find end marker!")
    exit(1)

# Include the closing `};` in the replaced section
end_idx += len(end_marker)

# Form the patched content
patched_html = (
    html_content[:start_idx]
    + new_modules_js
    + "\n\n    "
    + new_terminal_js
    + "\n"
    + html_content[end_idx:]
)

# Write patched content back to docker-k8s-guide.html
with open(html_path, "w", encoding="utf-8") as f:
    f.write(patched_html)

print("SUCCESS: Patched docker-k8s-guide.html successfully!")
