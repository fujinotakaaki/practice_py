import ui

def onAction(sender):
  label1 = sender.superview["label1"]
  label1.text = "You Tapped !!"

def onChange(sender):
  label1 = sender.superview["label1"]
  text1 = sender.superview['textfield1']
  label1.text = text1.text
  
v = ui.load_view()
v.present('sheet')
