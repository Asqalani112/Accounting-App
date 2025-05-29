import frappe


def make_gl_entries(entries: list):
    for entry in entries:
        gl = frappe.new_doc("GL Entry")
        gl.posting_date = entry.get("posting_date")
        gl.due_date = entry.get("due_date")
        gl.party = entry.get("party")
        gl.account = entry.get("account")
        gl.debit_amount = entry.get("debit_amount", 0)
        gl.credit_amount = entry.get("credit_amount", 0)
        gl.voucher_type = entry.get("voucher_type")
        gl.voucher_number = entry.get("voucher_number")
        gl.insert()