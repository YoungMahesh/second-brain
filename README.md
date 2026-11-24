# Second Brain

Knowledge vault organized using a modified Johnny Decimal / PARA taxonomy for software engineering, system architecture, tools, and domain knowledge.

## 🗂 Vault Taxonomy

### [10_Foundations](10_Foundations/README.md)
Core theoretical principles, computer science fundamentals, and protocol standards.
- **Computer Networking**: [Networking MOC](10_Foundations/computer-networking/moc_computer-networking.md), [HTTP](10_Foundations/computer-networking/HTTP.md), [osi-model](10_Foundations/computer-networking/osi-model.md), [tcp-ip-model](10_Foundations/computer-networking/tcp-ip-model.md), [DNS & Domains](10_Foundations/computer-networking/domain.md)
- **Web Protocols & Standards**: [CORS](10_Foundations/web/CORS.md), [OpenAPI](10_Foundations/web/OpenAPI.md), [swagger](10_Foundations/web/swagger.md), [MIME Types](10_Foundations/web/MIME%20Types.md), [reactjs](10_Foundations/web/reactjs/reactjs.md)
- **Languages**: [python](10_Foundations/languages/python/python.md), [javascript](10_Foundations/languages/typescript/javascript.md), [golang](10_Foundations/languages/golang.md), [html](10_Foundations/languages/html.md), [css](10_Foundations/languages/css.md), [zod](10_Foundations/languages/typescript/zod.md)
- **Databases**: [mysql](20_Tooling/docker/compose-files/mysql.md), [postgresql](10_Foundations/database/sql/postgres/postgresql.md), [drizzle-orm](10_Foundations/database/drizzle-orm/drizzle-orm.md), [mongodb](10_Foundations/database/mongodb.md), [turso](10_Foundations/database/sql/turso.md)
- **DSA**: [Algorithms List](10_Foundations/dsa/algorithm-list.md), [Concepts](10_Foundations/dsa/concepts.md), [sorting](10_Foundations/dsa/sorting/sorting.md), [heaps](10_Foundations/dsa/heaps/heaps.md), [trees](10_Foundations/dsa/graphs/trees.md)
- **Linux & OS**: [Ubuntu_os_installation](10_Foundations/linux/Ubuntu_os_installation.md), [ssh](10_Foundations/linux/ssh.md), [firewall](10_Foundations/linux/firewall.md), [i3wm](10_Foundations/linux/i3wm.md), [Remote GUI](10_Foundations/linux/Remote%20GUI.md), [userspace](10_Foundations/linux/userspace.md), [systemd](10_Foundations/linux/systemd/systemd.md)
- **System Design & Architecture**: [System Design Overview](10_Foundations/system_design/overview.md), [SOLID principles](10_Foundations/low-level_design/SOLID%20principles.md), [vcs (version control system)](10_Foundations/vcs/vcs%20%28version%20control%20system%29.md)

### 20_Tooling
Operational developer workflows, environments, command-line tools, and runtime configurations.
- **AI & Coding Agents**: [Antigravity](20_Tooling/ai/coding-agents/Antigravity%28agy%29.md), [claude code](20_Tooling/ai/coding-agents/claude%20code.md), [cursor](20_Tooling/ai/coding-agents/cursor.md), [github-copilot](20_Tooling/ai/coding-agents/github-copilot.md), [hermes-agent](20_Tooling/ai/coding-agents/hermes-agent.md), [openhands](20_Tooling/ai/coding-agents/openhands.md), [t3code](20_Tooling/ai/coding-agents/t3code.md), [OpenAI](20_Tooling/ai/providers/OpenAI.md)
- **CLI Tools**: [bash](20_Tooling/apps_CLI/terminal/bash.md), [zsh](20_Tooling/apps_CLI/zsh.md), [grep](20_Tooling/apps_CLI/grep.md), [sed](20_Tooling/apps_CLI/sed.md), [curl](20_Tooling/apps_CLI/curl.md), [ffmpeg](20_Tooling/apps_CLI/ffmpeg.md), [rclone](20_Tooling/apps_CLI/rclone.md), [Jujutsu](20_Tooling/apps_CLI/git/jj.md), [neovim](20_Tooling/apps_CLI/neovim.md)
- **GUI Applications**: [obsidian](20_Tooling/apps_GUI/obsidian.md), [firefox](20_Tooling/apps_GUI/firefox.md), [chromium](20_Tooling/apps_GUI/chromium.md), [remnote](20_Tooling/apps_GUI/remnote.md), [signal-desktop](20_Tooling/apps_GUI/signal-desktop.md)
- **Editors**: [vscode](20_Tooling/editors/vscode.md), [zed-editor](20_Tooling/editors/zed-editor.md), [windsurf](20_Tooling/editors/windsurf.md), [nano](20_Tooling/editors/nano.md), [vscode-keymaps](20_Tooling/editors/vscode-keymaps.md)
- **Containers & Orchestration**: [docker](20_Tooling/docker/docker.md), [docker-compose](20_Tooling/docker/docker-compose.md), [kubernetes](20_Tooling/docker/kubernetes.md), [traefik-proxy](20_Tooling/docker/domain/traefik-proxy.md)
- **Testing**: [playwright](20_Tooling/testing/playwright/playwright.md), [locators](20_Tooling/testing/playwright/locators/locators.md)
- **System & Hardware**: [bluetooth](20_Tooling/system/bluetooth.md), [audio](20_Tooling/system/audio.md), [keyboard](20_Tooling/system/keyboard.md), [snap-store](20_Tooling/system/snap-store.md), [system-setup](20_Tooling/system/system-setup.md)
- **Documentation Tools**: [docs-quartz](20_Tooling/docs/docs-quartz.md), [zensical](20_Tooling/docs/zensical.md), [mermaid-diagrams](20_Tooling/docs/mermaid-diagrams.md)

### 30_Domains
Specialized vertical domains, applied platforms, and production systems.
- **Authentication & Security**: [Auth Architecture](30_Domains/authentication/authentication.md), [better-auth](30_Domains/authentication/better-auth.md), [clerk-auth](30_Domains/authentication/clerk-auth.md), [OAuth 2.0](30_Domains/authentication/OAuth%202.0/OAuth%202.0.md)
- **Cloud & Infrastructure**: [cloudflare](30_Domains/cloud/cloudflare.md), [google-cloud](30_Domains/cloud/google-cloud.md), [modal.com](30_Domains/cloud/modal.com.md), [vps](30_Domains/cloud/vps.md)
- **Storage**: [s3-storage](30_Domains/storage/s3-storage.md), [minio](30_Domains/storage/minio.md), [seaweedfs](30_Domains/storage/seaweedfs.md), [s3cmd](30_Domains/storage/s3cmd.md)
- **Machine Learning & AI**: [machine-learning](30_Domains/ml/machine-learning.md), [llm](30_Domains/ml/llm.md), [embeddings](30_Domains/ml/embeddings.md), [vector](30_Domains/ml/vector.md), [ollama](30_Domains/ml/ollama.md), [datasets](30_Domains/ml/datasets.md)
- **SaaS & Services**: [notion](30_Domains/services/notion.md), [perplexity](30_Domains/services/perplexity.md), [youtube](30_Domains/services/youtube.md), [upwork](30_Domains/services/upwork.md), [proton-mail](30_Domains/services/proton-mail.md), [jio](30_Domains/services/jio.md)
- **Design & UI**: [excalidraw](30_Domains/design/excalidraw.md), [figma make](30_Domains/design/figma%20make.md), [getdesign](30_Domains/design/getdesign.md)
- **Mobile**: [react-native](30_Domains/react-native/react-native.md), [RN Architecture](30_Domains/react-native/architecture.md)
- **Web3 & Crypto**: [solana](30_Domains/web3/solana.md), [hardhat](30_Domains/web3/hardhat.md), [ipfs](30_Domains/web3/ipfs.md), [crypto-onramp](30_Domains/web3/crypto-onramp.md)
- **Payments**: [stripe](30_Domains/payments/stripe.md)

### 40_Resources
Curated bookmarks, reference cheat sheets, and external resources.
- **Bookmarks**: [bookmarks-web-development](40_Resources/bookmarks/bookmarks-web-development.md), [bookmarks-web-hosting](40_Resources/bookmarks/bookmarks-web-hosting.md), [bookmarks-editor](40_Resources/bookmarks/bookmarks-editor.md), [bookmarks-job](40_Resources/bookmarks/bookmarks-job.md), [bookmarks-learn](40_Resources/bookmarks/bookmarks-learn.md), [remote-sandboxes](40_Resources/bookmarks/remote-sandboxes.md)
- **Reference**: [emoji-codes](40_Resources/reference/emoji-codes.md)
