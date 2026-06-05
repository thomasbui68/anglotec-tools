import { useState, useEffect } from 'react';
import { Link } from 'react-router';
import { Menu, X } from 'lucide-react';

const navLinks = [
  { label: 'Home', path: '/' },
  { label: 'IELTS Calculator', path: '/ielts-calculator' },
  { label: 'OET Speaking', path: '/oet-speaking' },
  { label: 'OSCE Practice', path: '/osce-practice' },
  { label: 'AI Prompts', path: '/ai-prompt-generator' },
  { label: 'Language Guide', path: '/language-guide' },
];

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <>
      <nav
        className={`fixed top-0 left-0 right-0 z-50 h-[72px] flex items-center transition-all duration-300 ${
          isScrolled
            ? 'bg-[rgba(247,245,242,0.85)] backdrop-blur-[16px] border-b border-warm-gray shadow-xs'
            : 'bg-transparent'
        }`}
      >
        <div className="container-main w-full flex items-center justify-between">
          {/* Logo */}
          <Link to="/" className="flex items-center gap-2 shrink-0">
            <div className="w-8 h-8 rounded-lg bg-deep-green flex items-center justify-center">
              <span className="text-white font-heading font-bold text-sm">A</span>
            </div>
            <div className="flex flex-col">
              <span className={`font-heading font-bold text-lg leading-tight transition-colors duration-300 ${isScrolled ? 'text-deep-green' : 'text-white'}`}>
                Anglotec
              </span>
              <span className={`font-mono text-[9px] uppercase tracking-widest leading-none transition-colors duration-300 ${isScrolled ? 'text-muted-olive' : 'text-[rgba(255,255,255,0.6)]'}`}>
                AI Academy
              </span>
            </div>
          </Link>

          {/* Desktop Nav Links */}
          <div className="hidden lg:flex items-center gap-8">
            {navLinks.map((link) => (
              <Link
                key={link.path}
                to={link.path}
                className={`font-body font-medium text-sm transition-colors duration-200 link-underline ${
                  isScrolled
                    ? 'text-text-primary hover:text-burnt-orange'
                    : 'text-white hover:text-cream'
                }`}
              >
                {link.label}
              </Link>
            ))}
          </div>

          {/* CTA Button */}
          <div className="hidden lg:block">
            <a
              href="https://anglotec-ai.com/"
              target="_blank"
              rel="noopener noreferrer"
              className="btn-primary text-xs py-2.5 px-6"
            >
              Start Learning
            </a>
          </div>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setMobileOpen(!mobileOpen)}
            className={`lg:hidden p-2 rounded-lg transition-colors ${
              isScrolled ? 'text-text-primary' : 'text-white'
            }`}
            aria-label="Toggle menu"
          >
            {mobileOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
      </nav>

      {/* Mobile Drawer */}
      {mobileOpen && (
        <div className="fixed inset-0 z-[60]">
          <div
            className="absolute inset-0 bg-black/40 backdrop-blur-sm"
            onClick={() => setMobileOpen(false)}
          />
          <div className="absolute right-0 top-0 h-full w-[280px] bg-off-white shadow-2xl p-6 pt-20">
            <div className="flex flex-col gap-4">
              {navLinks.map((link) => (
                <Link
                  key={link.path}
                  to={link.path}
                  onClick={() => setMobileOpen(false)}
                  className="font-body font-medium text-text-primary py-2 border-b border-warm-gray hover:text-burnt-orange transition-colors"
                >
                  {link.label}
                </Link>
              ))}
              <a
                href="https://anglotec-ai.com/"
                target="_blank"
                rel="noopener noreferrer"
                className="btn-primary mt-4 text-center"
              >
                Start Learning
              </a>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
