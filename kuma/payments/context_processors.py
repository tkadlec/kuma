from .forms import ContributionForm
from .utils import enabled, popup_enabled


def global_contribution_form(request):
    """Adds contribution form to the context."""
    if enabled(request):
        return {
            'contribution_enabled': True,
            'contribution_popup': popup_enabled(request),
            'contribution_form': ContributionForm(),
            'hide_cta': True,
        }
    return {'contribution_enabled': False}
