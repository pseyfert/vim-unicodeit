# vim-unicodeit
a vim plugin around the backend code of unicodeit.net

## Installation

Follow the installation instructions of your favourite vim plugin manager.
Make sure git submodules are enabled and checked out as well.

## Usage

Check the contents of the `plugin/unicodeit.vim` file. By default, `^U u` is registered in visual mode (including visual line mode and visual block mode). It converts latex code in the highlighted region to unicode.

## Example

```
1 This is some file content
2 Here I write \alpha \neq  \psi.
```

When highlighting line 2 with `shift + V` and triggering the plugin `^U u` this turns into

```
1 This is some file content
2 Here I write α ≠ ψ.
```
