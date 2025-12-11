# Public Key to TXT File 🔑

A simple GitHub Action that saves a public key to a text file. This action is useful for workflows that need to export public keys to files for SSH configuration, deployment scripts, or other automation tasks.

## Features

- 📝 Save any public key content to a text file
- 📁 Automatically create output directories if needed
- 🎯 Configurable output file path
- ⚡ Simple and lightweight composite action

## Usage

### Basic Example

```yaml
name: Save Public Key
on: [push]

jobs:
  save-key:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      
      - name: Save public key to file
        uses: saeedahmed40/public-key-to-txt@v1
        with:
          public-key: ${{ secrets.MY_PUBLIC_KEY }}
          output-file: 'keys/public_key.txt'
```

### Advanced Example with Multiple Keys

```yaml
name: Save Multiple Keys
on: [push]

jobs:
  save-keys:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      
      - name: Save deployment key
        uses: saeedahmed40/public-key-to-txt@v1
        with:
          public-key: ${{ secrets.DEPLOY_PUBLIC_KEY }}
          output-file: '.ssh/deploy_key.pub'
      
      - name: Save backup key
        uses: saeedahmed40/public-key-to-txt@v1
        with:
          public-key: ${{ secrets.BACKUP_PUBLIC_KEY }}
          output-file: '.ssh/backup_key.pub'
      
      - name: Use the keys in subsequent steps
        run: |
          echo "Keys saved successfully!"
          cat .ssh/deploy_key.pub
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `public-key` | The public key content to save | Yes | - |
| `output-file` | The path where the public key file should be saved | No | `public_key.txt` |
| `create-directory` | Create the output directory if it does not exist | No | `true` |

## Outputs

| Output | Description |
|--------|-------------|
| `file-path` | The path to the created public key file |

### Using Outputs

```yaml
- name: Save public key
  id: save-key
  uses: saeedahmed40/public-key-to-txt@v1
  with:
    public-key: ${{ secrets.MY_PUBLIC_KEY }}
    output-file: 'my_key.pub'

- name: Display saved file path
  run: echo "Key saved at ${{ steps.save-key.outputs.file-path }}"
```

## Common Use Cases

### 1. SSH Key Configuration

```yaml
- name: Save SSH public key
  uses: saeedahmed40/public-key-to-txt@v1
  with:
    public-key: ${{ secrets.SSH_PUBLIC_KEY }}
    output-file: '~/.ssh/id_rsa.pub'

- name: Configure SSH
  run: |
    chmod 644 ~/.ssh/id_rsa.pub
    ssh-keygen -l -f ~/.ssh/id_rsa.pub
```

### 2. Deployment Keys

```yaml
- name: Save deployment key
  uses: saeedahmed40/public-key-to-txt@v1
  with:
    public-key: ${{ secrets.DEPLOY_KEY }}
    output-file: 'deploy/keys/deploy.pub'

- name: Deploy with key
  run: |
    ./deploy.sh --key deploy/keys/deploy.pub
```

### 3. Authorized Keys Setup

```yaml
- name: Save authorized key
  uses: saeedahmed40/public-key-to-txt@v1
  with:
    public-key: ${{ secrets.AUTHORIZED_KEY }}
    output-file: '.ssh/authorized_keys'

- name: Set permissions
  run: chmod 600 .ssh/authorized_keys
```

## Security Considerations

- 🔒 Always store public keys in GitHub Secrets, even though they are "public"
- 🛡️ Be careful with file permissions after saving keys
- ⚠️ Avoid committing generated key files back to the repository
- 🔐 Use appropriate `.gitignore` entries for key directories

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/saeedahmed40/public-key-to-txt/issues) on GitHub.