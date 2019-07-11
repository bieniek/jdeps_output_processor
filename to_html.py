import sys

start = """
<html>
    <head>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <style>
        body {
  font-family: Helvetica, sans-serif;
  font-size:15px;
}

a {
  text-decoration:none;
}
ul.tree, .tree li {
    list-style: none;
    margin:0;
    padding:0;
    cursor: pointer;
}

.tree ul {
  display:none;
}

.tree > li {
  display:block;
  background:#eee;
  margin-bottom:2px;
}

.tree span {
  display:block;
  padding:10px 12px;

}

.icon {
  display:inline-block;
}

.tree .hasChildren > .expanded {
  background:#999;
}

.tree .hasChildren > .expanded a {
  color:#fff;
}

.icon:before {
  content:"+";
  display:inline-block;
  min-width:20px;
  text-align:center;
}
.tree .icon.expanded:before {
  content:"-";
}

.show-effect {
  display:block!important;
}
.space {
    width:20px;
    display:inline-block;
}
.space:before {
  content:" ";
  display:inline-block;
  min-width:20px;
  text-align:center;  
}
    </style>
    </head>
    <body>
    <ul class="tree">
"""
end = """       
    </ul>
 <script type="text/javascript">
    $('.tree .icon').click( function() {
      $(this).parent().toggleClass('expanded').closest('li').find('ul:first').toggleClass('show-effect');
    });
</script>

    </body>
</html>
"""

def count_spaces(line):
    return len(line) - len(line.lstrip(' '))

def get_with_children(line):
    result = '<li class="tree__item hasChildren">'
    result += '<span><div class="icon"></div><a href="#">' + line + '</a></span>'
    result += '<ul>'
    return result
   
def get(line):
    result = '<li>'
    result += '<span><div class="space">&nbsp;</div><a href="#">' + line + '</a></span>'
    result += '</li>'
    return result

body = ""
spaces_num = 0
prev_line = ""
for line in sys.stdin:
    if prev_line == "":
        prev_line = line
        prev_tt = count_spaces(line)
    else:
        tt = count_spaces(line)
        if tt > prev_tt:
            body += get_with_children(prev_line)
        elif tt < prev_tt:
            body += get(prev_line)
            diff = prev_tt - tt
            for i in range(diff): 
                body += '</ul>'
                body += "</li>"    
        else:
            body += get(prev_line)

        prev_tt = tt
        prev_line = line

print start + body + end

