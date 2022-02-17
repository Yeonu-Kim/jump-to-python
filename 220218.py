import game.sound.echo
game.sound.echo.echo_test()
#Echo

from game.sound.echo import echo_test
echo_test()
#Echo

from game.sound import echo
echo.echo_test()
#Echo

#import game
#game.sound.echo.echo_test()
#Traceback (most recent call last):
#  File "c:\doit\package.py", line 14, in <module>
#    game.sound.echo.echo.test()
#AttributeError: module 'game.sound.echo' has no attribute 'echo'

#import game.sound.echo.echo_test()
#  File "c:\doit\package.py", line 20
#    import game.sound.echo.echo_test()
#                                    ^
#SyntaxError: invalid syntax

from game.sound import *
echo.echo_test()
#Echo
#?? 에코 잘 나오는디? 업데이트 됐나?

from game.graphic import *
render.render_test()
#Traceback (most recent call last):
#  File "c:\doit\package.py", line 32, in <module>
#    render.render_test()
#NameError: name 'render' is not defined

#render은 nameError 발생
#__all__로 처리 가능
