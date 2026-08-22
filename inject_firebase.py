import glob
import re

files = glob.glob('d:/Users/expor/Downloads/Codes/gemini-code-*.html')

injection_script = '''
<!-- FIREBASE INJECTION START -->
<script type="module">
    import { db, doc, onSnapshot } from './firebase-config.js';
    
    // Listen for answer lock/unlock
    const settingsDoc = doc(db, 'settings', 'global');
    onSnapshot(settingsDoc, (docSnap) => {
        const data = docSnap.data() || { showAnswers: true };
        
        // Find all buttons that might reveal answers
        const buttons = Array.from(document.querySelectorAll('button')).filter(b => {
            const text = b.textContent.toLowerCase();
            return text.includes('reveal') || text.includes('answer') || text.includes('check');
        });

        if (data.showAnswers === false) {
            // Lock them
            buttons.forEach(b => {
                b.style.display = 'none';
            });
            
            // Add a locked message if not exists
            if (!document.getElementById('lock-msg')) {
                const msg = document.createElement('div');
                msg.id = 'lock-msg';
                msg.style.padding = '15px';
                msg.style.margin = '20px 0';
                msg.style.backgroundColor = '#f8d7da';
                msg.style.color = '#721c24';
                msg.style.border = '1px solid #f5c6cb';
                msg.style.borderRadius = '5px';
                msg.style.fontWeight = 'bold';
                msg.textContent = '🔒 Answers are currently locked by the Parent Administrator.';
                document.body.appendChild(msg);
            } else {
                document.getElementById('lock-msg').style.display = 'block';
            }
        } else {
            // Unlock them
            buttons.forEach(b => {
                b.style.display = 'inline-block';
            });
            if (document.getElementById('lock-msg')) {
                document.getElementById('lock-msg').style.display = 'none';
            }
        }
    });
</script>
<!-- FIREBASE INJECTION END -->
'''

for f in files:
    with open(f, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
        
    if 'FIREBASE INJECTION START' not in content:
        content = content.replace('</body>', injection_script + '\n</body>')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
            
print("Successfully injected Firebase listener into all chapter files.")
