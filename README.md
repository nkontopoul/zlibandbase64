# zlibandbase64
Αποκωδικοποίηση συμπιεσμένου κειμένου από malware που προήλθε από zlib+base64 encoding

Ψάχνοντας τα string κάποιου από τα πρόσφατα ransomware/malware ενδεχομένως να ανακαλύψετε πως τμήματα που μοιάζουνε να έχουν κωδικοποιηθεί με base64  δεν αποκωδικοποιούνται με τα γνωστά online εργαλεία. 
Πιθανόν να έχουν υποστεί συμπίεση με το zlib ώστε να μη μπορεί να τα βρεί κάποιο εργαλείο αναζήτησης ή κάποιος που παρατηρεί τον κώδικα. Οπότε δε τα παρατάμε.
Με τον παρακάτω απλό κώδικα σε python θα μπορούσαμε να δοκιμάσουμε και να αποκωδικοποιήσουμε τέτοια μηνύματα που έχουν υποστεί base64 encoding+zlib encoding:
