frappe.ui.form.on('Customer Visit Log', {
    refresh(frm) {
        // ตัวอย่าง: alert เมื่อเปิดฟอร์ม
        console.log('Custom JS loaded!');
        frappe.msgprint('Welcome to Customer Visit Log!888');
    }
});