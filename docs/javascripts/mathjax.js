/* MathJax config for Material + mkdocs-jupyter.
 *
 * Approach: process the whole page (not only .arithmatex).
 * Material's usual ignoreHtmlClass:".*|" + processHtmlClass:"arithmatex"
 * works for Markdown pages (arithmatex wraps $/$/), but mkdocs-jupyter
 * emits notebook markdown as raw $...$ / $$...$$ without that class —
 * MathJax then skips those cells and users see literal LaTeX.
 *
 * We keep $/$$ and \(/\)/\[/\] delimiters, skip code-like tags, and
 * let both .md pages and notebook HTML typeset.
 */
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
  },
  options: {
    skipHtmlTags: ["script", "noscript", "style", "textarea", "pre", "code"],
    ignoreHtmlClass: "tex2jax_ignore|mathjax_ignore|no-mathjax",
  },
};
