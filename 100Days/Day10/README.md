# tkinter相关参数解释

## 使用方式  
### 一般通过以下方式导入
`import tkinter`  
### 或者,通过如下方式  
`from tkinter import *`  

## 介绍一些类  
* Wm:Windows manager 窗口管理  
* Misc:内置方法定义内部部件常用方法的基类  
* Variable:变量,子类有:  
  * StringVar  
  * IntVar
  * DoubleVar
  * BooleanVar
* CallWrapper:  
  * Tk:构件
  * Pack: 位置填充
  * Place: 位置设定  
  * BaseWidget: 基础构件  

## 相关函数  
* tkinter.scrolledtext  
>Text widget with a vertical scroll bar built in.  
>内置垂直滚动条的文本小部件  

* tkinter.colorchooser  
>Dialog to let the user choose a color.  
>让用户选择颜色的对话框  

* tkinter.commondialog  
>Base class for the dialogs defined in the other modules listed here.  
>其他模块中定义的对话框的基类  

* tkinter.filedialog  
>Common dialogs to allow the user to specify a file to open or save.  
>允许用户指定要打开或保存的文件的通用对话框  

* tkinter.font  
>Utilities to help work with fonts.  
>帮助字体工作的实用工具  

* tkinter.messagebox  
>Access to standard Tk dialog boxes.  
>访问标准TK对话框  

* tkinter.simpledialog  
>Basic dialogs and convenience functions.  
>基本对话框和方便功能  

* tkinter.dnd  
>Drag-and-drop support for tkinter. This is experimental and should become deprecated when it is replaced with the Tk DND.  
>Tkinter支持拖放。但是，这是实验性的。应该成为过时的，应当被TK DND取代  

* turtle  
>Turtle graphics in a Tk window.  
>海龟空间在Tk窗口中

***  

## Place  
### 设置控件的位置,以坐标方式进行  
>place是最简单的几何形状的管理，在Tkinter提供的三个通用几何图形管理。
它允许显式地设置窗口的位置和大小，无论是绝对值，还是相对于另一个窗口。
通常不会使用place来管理窗口控件的位置，它只是为了让工作变得简单，正常工作。
一般推荐使用pack和grid方式来进行控件控制。
然而，place在特殊情况下有其用途。最重要的是，它可以由复合小部件容器实现各种自定义几何管理器。另一个用途是在对话框中放置控制按钮，实现不同控件的覆盖。  

* place(options)[#]  
>Place this widget relative to its parent.  
* options  
  * anchor= #  
  >锚，停靠的地方，默认是：图形位置的西北;默认值是 NW.  
  * bordermode= #  
  >边框模式，默认是：内边界;默认值是 INSIDE.  
  * height= #  
  >高度,无默认值.  
  * in= #  
  >控制在某个控件内，in是python中的关键字，通常使用 in_ 代替;默认值是 ..  
  * relheight= #  
  >相对高度;无默认值.  
  * relwidth= #  
  >相对宽度;无默认值.  
  * relx= #  
  >相对水平距离;默认值是 0.  
  * rely= #  
  >相对垂直距离;默认值是 0.  
  * width= #  
  >宽度;无默认值.  
  * x= #  
  >相对于水平的距离，以像素为单位;默认值是 0.  
  * y= #  
  >相对于垂直的距离，以像素为单位,默认值是 0.  
  
## Pack  
### 控件内的填充，一般会是填充整个控件  
>相比于grid管理，pack管理是有所限制的，但它更容易使用一些。  
1.将一个小部件放入框架（或任何其他容器小部件）中，并填充整个框架。  
2.将许多小部件放在彼此之上。  
3.并排放置多个小部件。  
如果你需要创建更复杂的布局，通常你需要使用额外的框架部件的部件组。你也可以使用网格管理器代替。  
注意：不要在同一主窗口中混合使用grid和pack。tkinter无法兼顾到两种。  

* pack(options)[#]  

* options  
  * anchor= #  
  >将小部件放在pack。默认位置为中心 CENTER ，其他的还有N,NE,E,SE,S,SW,W,NW, CENTER.  
  * expand= #  
  >指定是否应扩展小部件以填充几何主机中的任何额外空间。如果为false（默认），则未扩展小部件.  
  * fill= #  
  >指定小部件是否应该占用主提供给它的所有空间。如果NONE没有（默认），保留小部件的原始大小。如果x（水平填充），y（垂直填充），或者 BOTH 两者都，沿着这个方向填充给定的空间。要使一个小部件填充整个主窗口小部件，将填充设置为两个，然后扩展到非零值。  
  * in= #  
  >将此小部件打包到给定的小部件内。你只能装在它的父控件，或在任何后学其父。这个选项通常应该被忽略，在这种情况下，小部件被打包在其父进程内.  注意，在Python中是一个保留字。使用它作为一个关键词的选择，添加一个下划线（in_）.
  * ipadx= #  
  >水平内部填充。默认值是0.  
  * ipady= #  
  >垂直内部填充。默认值是0.  
  * padx= #  
  >水平扩展，外部填充。默认值是0.  
  * pady= #  
  >垂直扩展，外部填充。默认值是0.  
  * side= #  
  >指定包装小部件的哪一面。要垂直包装小部件，使用TOP（默认）。要横向包装小部件，请使用LEFT。
您还可以沿着（BOTTOM and RIGHT）右下角包装小部件。您可以在一个单一的几何管理器中混合边，但结果可能并不总是您期望的那样。虽然可以通过嵌套框架小部件来创建相当复杂的布局，但您可能更喜欢使用网格几何管理器来实现不平凡的布局.  

## Grid  
### 以网格的方式进行设置控件位置    

* grid(options)[#]  
* options  
  * column= #  
  >在当前列插入一个小器件，列的其实数字是0，如果不设置，默认为0. 
  * columnspan= #  
  >如果给定，则指示小部件单元应该跨越多个列。默认值是1.  
  * in= #  
  >将小部件放入给定的部件中。你只能放置一个控件在其父控件上，或任何其父控件的子控件中。如果不提供此选项，则默认为父级.  注意，在Python中是一个保留字。使用它作为一个关键词的选择，添加一个下划线（in_）.
  * in_= #  
  >同上  
  * ipadx= #  
  >可选水平内填充。就像padx，但填充里面的控件的边界。默认值是0.  
  * ipady= #  
  >可选垂直内填充。就像pady，但填充里面的控件的边界。默认值是0.  
  * padx= #  
  >可选的水平填充，以放置在单元格中的小部件周围。默认值是0.  
  * pady= #  
  >可选的垂直填充，以放置在单元格中的小部件周围。默认值是0.  
  * row= #  
  >在这行插入小部件。行号从0开始。如果省略，则默认为网格中的第一个空行.  
  * rowspan= #  
  >如果给定，则指示小部件单元应该跨越多行。默认值是1.  
  * sticky= #  
  >定义如何扩展小部件，如果生成的单元格大于小部件本身。这可以是常数S, N, E,和W ，也可以是任意组合NW、NE、SW和SE。
例如，W (west) 意味着小部件应该与左单元格边界对齐。W+E意味着小部件应该水平拉伸以填充整个单元。W+E+N+S意味着小部件应该在两个方向上展开，平铺在单元格内。默认是将小部件居中.    

