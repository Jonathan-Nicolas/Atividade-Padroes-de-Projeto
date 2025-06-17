# Atividade — Padrões de Projeto

## Padrão Aplicado: Chain of Responsibility (Cadeia de Responsabilidade)

Este projeto demonstra a aplicação do padrão de projeto comportamental **Chain of Responsibility**.  
Originalmente, o código foi criado para renomear arquivos de músicas baixadas dos sites:

- [https://spotify-downloader.com/](https://spotify-downloader.com/) - antigo
- [https://spotdownloader.com/](https://spotdownloader.com/)

---

## 💡 Como Executar

1. Crie uma pasta chamada `spotfy_playlist` no mesmo diretório onde está o arquivo `chain_of_responsibility.py`.
2. Baixe uma playlist de um dos sites acima.
3. Extraia o conteúdo `.rar` dentro da pasta `spotfy_playlist`. Após a extração, os arquivos de música devem estar diretamente dentro dessa pasta.
4. Execute o script `chain_of_responsibility.py`.
   
---

## ✅ Funcionalidades

- Remove a propaganda `[SPOTIFY-DOWNLOADER.COM]` dos nomes dos arquivos.
- Substitui `_` e `-` por espaços.
- Aplica capitalização em cada palavra do nome (formato *Title Case*).

---

## 🛠️ Observações

Os sites de download podem sair do ar ou mudar de nome com o tempo.  
No arquivo `Validadores/site_name_handler.py`, você pode adicionar regras personalizadas para tratar novos formatos ou domínios.

Já foi implementada uma **expressão regular** que captura padrões como `"[...]"`, mas vale o aviso: não sabemos o que o futuro nos reserva — rsrs.

---

**Obrigado por ler ❤️**
